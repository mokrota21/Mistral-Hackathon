from llm_agent.llm_agent import analyze_chunks_parallel
from chunks_service import DefaultChunker
from llm_agent.state import KnowledgeObject

from asyncio import run
from typing import List
from paths import KNOWLEDGE_OBJECTS_PATH, CHUNKS_PATH
import logging
import sys
import json
from random import sample

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    force=True,
)
logger = logging.getLogger(__name__)


# ── Versioned knowledge storage helpers ──
# Path layout: data/knowledge_objects/{book_name}/{provider}/0.json, 1.json, ...

def _book_ko_dir(textbook_name: str, provider: str = "mistral"):
    """Return the directory for a book+provider's knowledge versions."""
    return KNOWLEDGE_OBJECTS_PATH / textbook_name / provider


def _next_ko_index(textbook_name: str, provider: str = "mistral") -> int:
    """Find the next version index (max existing + 1)."""
    ko_dir = _book_ko_dir(textbook_name, provider)
    if not ko_dir.exists():
        return 0
    existing = [int(f.stem) for f in ko_dir.glob("*.json") if f.stem.isdigit()]
    return max(existing) + 1 if existing else 0


def _latest_ko_path(textbook_name: str, provider: str = "mistral"):
    """Return path to the latest knowledge version, or None if none exist."""
    ko_dir = _book_ko_dir(textbook_name, provider)
    if not ko_dir.exists():
        return None
    existing = [f for f in ko_dir.glob("*.json") if f.stem.isdigit()]
    if not existing:
        return None
    return max(existing, key=lambda f: int(f.stem))


def analyze_textbook(textbook_name: str, limit: int = 10, provider: str = "mistral") -> None:
    chunks_path = CHUNKS_PATH / f"{textbook_name}.json"

    assert chunks_path.exists(), f"Chunks path {chunks_path} does not exist"
    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    chunks_text = [c["text"] for c in chunks]
    chunks_pages = [c["page_no"] for c in chunks]
    chunks_text = chunks_text[:limit]
    chunks_pages = chunks_pages[:limit]
    knowledge_objects = run(analyze_chunks_parallel(chunks_text, chunks_pages, provider=provider))
    knowledge_objects_json = [k.model_dump(mode='dict') for k in knowledge_objects]

    # Save to versioned path: data/knowledge_objects/{book_name}/{provider}/{index}.json
    ko_dir = _book_ko_dir(textbook_name, provider)
    ko_dir.mkdir(parents=True, exist_ok=True)
    idx = _next_ko_index(textbook_name, provider)
    output_path = ko_dir / f"{idx}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(knowledge_objects_json, f, indent=4)
    logger.info(f"Textbook {textbook_name} analyzed with provider={provider}. {len(knowledge_objects)} knowledge objects saved to version {idx}")


def fetch_relevant_knowledge(textbook_name: str, limit: int = 10, current_page: int = 0, provider: str = "mistral") -> List[KnowledgeObject]:
    ko_path = _latest_ko_path(textbook_name, provider)
    assert ko_path is not None, f"No knowledge objects found for {textbook_name} (provider={provider})"
    with open(ko_path, "r", encoding="utf-8") as f:
        knowledge_objects = json.load(f)
    relevant_objects = [o for o in knowledge_objects if o["reference"] <= current_page]
    return sample(relevant_objects, min(limit, len(relevant_objects)))
