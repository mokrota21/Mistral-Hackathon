from pathlib import Path
from chunks_service import DefaultChunker
from llm_agent.state import ChunkAnalysisResponse
from config import settings
from paths import KNOWLEDGE_OBJECTS_PATH, TEXTBOOK_PATH
from asyncio import run, Semaphore, Lock, gather
from enum import Enum
import logging
import json
import sys
from pydantic import BaseModel, Field

# Avoid "charmap codec can't encode" on Windows when logging/printing Unicode
try:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
        sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    force=True,
)
logger = logging.getLogger("generate_data_service")

# Reuse the same prompt file as llm_agent
_prompt_path = Path(__file__).parent / "llm_agent" / "prompts" / "general-textbook.txt"
with open(_prompt_path, encoding="utf-8") as f:
    PROMPT = f.read()

SYSTEM_MESSAGE = "You are an expert at analyzing educational content and extracting important knowledge that students should remember."


async def generate_and_save(
    chunk: str,
    chunk_idx: int,
    total: int,
    file,
    semaphore: Semaphore,
    write_lock: Lock,
) -> bool:
    """
    Sends a chunk to mistral-large, appends the training example
    to the open file immediately, and returns True on success.
    """
    async with semaphore:
        try:
            model = settings.teacher_llm_client.with_structured_output(ChunkAnalysisResponse)
            user_content = PROMPT.format(current_chunk=chunk)

            messages = [
                {"role": "system", "content": SYSTEM_MESSAGE},
                {"role": "user", "content": user_content},
            ]

            parsed: ChunkAnalysisResponse = await model.ainvoke(messages)

            example = {
                "messages": [
                    {"role": "system", "content": SYSTEM_MESSAGE},
                    {"role": "user", "content": user_content},
                    {"role": "assistant", "content": parsed.model_dump_json()},
                ]
            }

            async with write_lock:
                file.write(json.dumps(example, ensure_ascii=False) + "\n")
                file.flush()

            logger.info(f"Chunk {chunk_idx + 1}/{total} saved")
            return True
        except Exception as e:
            logger.error(f"Chunk {chunk_idx + 1}/{total} failed: {e}", exc_info=True)
            return False


async def generate_dataset(chunks: list[str], output_path: Path, max_concurrent: int = 5) -> int:
    semaphore = Semaphore(max_concurrent)
    write_lock = Lock()

    with open(output_path, "a", encoding="utf-8") as f:
        tasks = [
            generate_and_save(chunk, i, len(chunks), f, semaphore, write_lock)
            for i, chunk in enumerate(chunks)
        ]
        results = await gather(*tasks, return_exceptions=True)

    succeeded = sum(1 for r in results if r is True)
    return succeeded


def generate_synthetic_data(
    book_path: Path,
    limit_chunks: int = 10,
    output_path: Path = None,
) -> None:
    with open(book_path, encoding="utf-8", mode="r") as file:
        textbook_text = file.read()

    chunker = DefaultChunker()
    logger.info("Chunking book...")
    chunks = [c["text"] for c in chunker.chunk([textbook_text])]
    logger.info(f"Total chunks: {len(chunks)}, using first {limit_chunks}")
    chunks = chunks[:limit_chunks]

    output_path = output_path or (KNOWLEDGE_OBJECTS_PATH.parent / "training_dataset.jsonl")
    logger.info(f"Generating training data from {len(chunks)} chunks via mistral-large...")
    logger.info(f"Appending to {output_path}")

    succeeded = run(generate_dataset(chunks, output_path))
    logger.info(f"Done: {succeeded}/{len(chunks)} chunks saved to {output_path}")

class Grade(str, Enum):
    GOOD = "good"
    BAD = "bad"


class KnowledgeGrade(BaseModel):
    knowledge_object: str = Field(..., description="The topic name of the knowledge object being graded")
    grade: Grade = Field(..., description="'good' if relevant to the book's subject matter, 'bad' if meta/irrelevant")


class KnowledgeGradeList(BaseModel):
    grades: list[KnowledgeGrade] = Field(..., description="List of grades, one per knowledge object, in the same order as the input")


_grade_prompt_path = Path(__file__).parent / "llm_agent" / "prompts" / "grade-knowledge.txt"
with open(_grade_prompt_path, encoding="utf-8") as f:
    GRADE_PROMPT = f.read()

_book_desc_path = Path(__file__).parent / "llm_agent" / "prompts" / "book-description.txt"
with open(_book_desc_path, encoding="utf-8") as f:
    BOOK_DESCRIPTION = f.read()


async def grade_knowledge_objects(knowledge_objects: list[dict], semaphore: Semaphore) -> list[Grade]:
    """Call the teacher LLM to grade a batch of knowledge objects as good/bad."""
    async with semaphore:
        formatted_objects = "\n".join(
            f"{i+1}. Topic: {obj['knowledge_object']}\n   Question: {obj['question']}"
            for i, obj in enumerate(knowledge_objects)
        )
        user_content = GRADE_PROMPT.format(
            book_description=BOOK_DESCRIPTION,
            knowledge_objects=formatted_objects,
        )
        model = settings.teacher_llm_client.with_structured_output(KnowledgeGradeList)
        result: KnowledgeGradeList = await model.ainvoke([
            {"role": "system", "content": "You are a strict quality-control reviewer for educational training data."},
            {"role": "user", "content": user_content},
        ])
        return [g.grade for g in result.grades]


async def filter_single_example(
    line: str,
    line_idx: int,
    total: int,
    file,
    semaphore: Semaphore,
    write_lock: Lock,
) -> bool:
    """Grade knowledge objects in one JSONL line, append the filtered result immediately."""
    try:
        example = json.loads(line)
        assistant_msg = example["messages"][-1]
        parsed = json.loads(assistant_msg["content"])
        objects = parsed.get("knowledge_objects", [])

        if not objects:
            return False

        grades = await grade_knowledge_objects(objects, semaphore)

        if len(grades) != len(objects):
            logger.warning(f"Line {line_idx+1}: got {len(grades)} grades for {len(objects)} objects, keeping all")
            kept = objects
        else:
            kept = [obj for obj, grade in zip(objects, grades) if grade == Grade.GOOD]

        removed = len(objects) - len(kept)
        logger.info(f"Line {line_idx+1}/{total}: kept {len(kept)}/{len(objects)} objects (removed {removed})")

        if not kept:
            return False

        parsed["knowledge_objects"] = kept
        assistant_msg["content"] = json.dumps(parsed, ensure_ascii=False)

        async with write_lock:
            file.write(json.dumps(example, ensure_ascii=False) + "\n")
            file.flush()

        return True

    except Exception as e:
        logger.error(f"Line {line_idx+1}/{total} grading failed: {e}", exc_info=True)
        return False


async def filter_dataset(data_path: Path, max_concurrent: int = 5) -> Path:
    """Read a JSONL training file, grade every knowledge object, write a _filtered version."""
    stem = data_path.stem
    filtered_path = data_path.with_name(f"{stem}_filtered{data_path.suffix}")

    with open(data_path, encoding="utf-8") as f:
        lines = [l for l in f if l.strip()]

    logger.info(f"Filtering {len(lines)} examples from {data_path.name} ...")
    semaphore = Semaphore(max_concurrent)
    write_lock = Lock()

    with open(filtered_path, "a", encoding="utf-8") as f:
        tasks = [
            filter_single_example(line, i, len(lines), f, semaphore, write_lock)
            for i, line in enumerate(lines)
        ]
        results = await gather(*tasks, return_exceptions=True)

    succeeded = sum(1 for r in results if r is True)
    logger.info(f"Filtered dataset saved to {filtered_path}")
    logger.info(f"Kept {succeeded}/{len(lines)} examples")
    return filtered_path


if __name__ == "__main__":
    import argparse as _ap

    parser = _ap.ArgumentParser()
    parser.add_argument("--mode", choices=["generate", "filter"], default="generate")
    parser.add_argument("--data", default=None, help="Path to JSONL file (for filter mode)")
    parser.add_argument("--limit", type=int, default=20000)
    args = parser.parse_args()

    if args.mode == "generate":
        generate_synthetic_data(TEXTBOOK_PATH, limit_chunks=args.limit)
    elif args.mode == "filter":
        data_path = Path(args.data) if args.data else (KNOWLEDGE_OBJECTS_PATH.parent / "training_dataset.jsonl")
        run(filter_dataset(data_path))
