from config import settings
from llm_agent.state import ChunkAnalysisResponse, ChunkKnowledge, KnowledgeObject
import json
import logging
import asyncio
import re
from pathlib import Path
from typing import List

logger = logging.getLogger("llm_agent")

# Get the directory where this file is located
_current_dir = Path(__file__).parent
_prompt_path = _current_dir / "prompts" / "general-textbook.txt"
with open(_prompt_path, encoding='utf-8') as f:
    PROMPT = f.read()


def _extract_json_from_text(text: str) -> dict | None:
    """Try to extract a JSON object from raw LLM output (handles markdown fences, etc.)."""
    # Strip markdown code fences if present
    text = text.strip()
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if match:
        text = match.group(1).strip()

    # Try to find the outermost JSON object
    for start in range(len(text)):
        if text[start] == "{":
            try:
                obj = json.loads(text[start:])
                return obj
            except json.JSONDecodeError:
                continue
    return None


async def _analyze_chunk_finetuned(chunk: str, chunk_reference: int, provider: str) -> ChunkKnowledge:
    """
    Analyse with the fine-tuned local model.

    Uses json_mode first (LangChain parses message.content as JSON).
    Falls back to raw completion + manual JSON extraction if structured output fails,
    because small fine-tuned models sometimes produce slightly malformed JSON.
    """
    model = settings.get_llm_client(provider)
    user_content = PROMPT.format(current_chunk=chunk)

    system_msg = (
        "You are an expert at analyzing educational content and extracting important knowledge "
        "that students should remember. Always respond with valid JSON."
    )
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_content},
    ]

    # Attempt 1: structured output with json_mode
    try:
        model_with_structure = model.with_structured_output(
            ChunkAnalysisResponse, method="json_mode"
        )
        parsed_response = await model_with_structure.ainvoke(
            messages,
            config={"callbacks": [settings.langfuse_handler]},
        )
        return ChunkKnowledge(
            knowledge_objects=parsed_response.knowledge_objects,
            reference=chunk_reference,
        )
    except Exception as e:
        logger.warning(f"Fine-tuned json_mode failed, falling back to raw parsing: {e}")

    # Attempt 2: raw completion + manual JSON extraction
    raw_response = await model.ainvoke(
        messages,
        config={"callbacks": [settings.langfuse_handler]},
    )
    raw_text = raw_response.content if hasattr(raw_response, "content") else str(raw_response)
    logger.debug(f"Fine-tuned raw output: {raw_text[:500]}")

    obj = _extract_json_from_text(raw_text)
    if obj is not None:
        try:
            parsed = ChunkAnalysisResponse.model_validate(obj)
            return ChunkKnowledge(
                knowledge_objects=parsed.knowledge_objects,
                reference=chunk_reference,
            )
        except Exception as parse_err:
            logger.error(f"JSON found but schema validation failed: {parse_err}")
    else:
        logger.error(f"Could not extract JSON from fine-tuned response: {raw_text[:300]}")

    return None


async def analyze_chunk(chunk: str, chunk_reference: int = -1, provider: str = None) -> ChunkKnowledge:
    """
    Analyzes single chunk on presence of any review interesting information

    Args:
        chunk: Text chunk to analyze
        chunk_reference: Reference identifier for the chunk (e.g., chunk index or page number)
        provider: LLM provider to use (e.g., "mistral", "fine-tuned"). Defaults to config setting.

    Returns:
        ChunkKnowledge object
    """
    effective_provider = provider or settings.llm_provider

    # Fine-tuned models need special handling (no tool-calling support)
    if effective_provider == "fine-tuned":
        return await _analyze_chunk_finetuned(chunk, chunk_reference, provider)

    try:
        model = settings.get_llm_client(provider)
        model_with_structure = model.with_structured_output(ChunkAnalysisResponse)

        # Format prompt with chunk content
        user_content = PROMPT.format(current_chunk=chunk)

        messages = [
            {"role": "system", "content": "You are an expert at analyzing educational content and extracting important knowledge that students should remember."},
            {"role": "user", "content": user_content}
        ]

        parsed_response = await model_with_structure.ainvoke(
            messages,
            config={
                "callbacks": [settings.langfuse_handler],
            }
        )

        return ChunkKnowledge(
            knowledge_objects=parsed_response.knowledge_objects,
            reference=chunk_reference
        )
    except Exception as e:
        logger.error(f"Error analyzing chunk: {e}", exc_info=True)
        return None


async def analyze_chunks_parallel(
    chunks: List[str],
    chunk_references: List[int] = None,
    batch_size: int = 10,
    max_concurrent: int = 5,
    provider: str = None,
) -> List[ChunkKnowledge]:
    """
    Analyzes a list of chunks in parallel batches and returns aggregated results.

    Args:
        chunks: List of text chunks to analyze
        chunk_references: Optional list of reference identifiers for each chunk
        batch_size: Number of chunks to process in each batch
        max_concurrent: Maximum number of concurrent requests per batch
        provider: LLM provider to use (e.g., "mistral", "fine-tuned")

    Returns:
        AgentResponse with aggregated knowledge_list and errors from all chunks
    """
    if chunk_references is None:
        chunk_references = [f"chunk_{i}" for i in range(len(chunks))]

    if len(chunks) != len(chunk_references):
        raise ValueError("chunks and chunk_references must have the same length")

    all_knowledge: List[ChunkKnowledge] = []

    # Process chunks in batches
    for batch_start in range(0, len(chunks), batch_size):
        batch_end = min(batch_start + batch_size, len(chunks))
        batch_chunks = chunks[batch_start:batch_end]
        batch_references = chunk_references[batch_start:batch_end]

        logger.info(f"Processing batch {batch_start // batch_size + 1}: chunks {batch_start} to {batch_end - 1}")

        # Create semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(max_concurrent)

        async def analyze_with_semaphore(chunk: str, ref: int):
            async with semaphore:
                return await analyze_chunk(chunk, ref, provider=provider)
        
        # Process batch in parallel
        tasks = [
            analyze_with_semaphore(chunk, ref) 
            for chunk, ref in zip(batch_chunks, batch_references)
        ]
        
        batch_results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in batch_results:
            if result is not None:
                all_knowledge.append(result)
    
    logger.info(f"Completed processing {len(chunks)} chunks. Found {len(all_knowledge)} knowledge items")
    
    return all_knowledge
