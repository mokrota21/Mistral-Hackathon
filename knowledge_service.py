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


def analyze_textbook(textbook_name: str, limit: int = 10) -> None:
    chunks_path = CHUNKS_PATH / f"{textbook_name}.json"

    assert chunks_path.exists(), f"Chunks path {chunks_path} does not exist"
    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    chunks_text = [c["text"] for c in chunks]
    chunks_pages = [c["page_no"] for c in chunks]
    chunks_text = chunks_text[:limit]
    chunks_pages = chunks_pages[:limit]
    knowledge_objects = run(analyze_chunks_parallel(chunks_text, chunks_pages))
    knowledge_objects_json = [k.model_dump(mode='dict') for k in knowledge_objects]
    
    with open(KNOWLEDGE_OBJECTS_PATH / f"{textbook_name}.json", "w", encoding="utf-8") as f:
        json.dump(knowledge_objects_json, f, indent=4)
    logger.info(f"Textbook {textbook_name} analyzed. {len(knowledge_objects)} knowledge objects found")

def fetch_relevant_knowledge(textbook_name: str, limit: int = 10, current_page: int = 0) -> List[KnowledgeObject]:
    knowledge_objects_path = KNOWLEDGE_OBJECTS_PATH / f"{textbook_name}.json"
    assert knowledge_objects_path.exists(), f"Knowledge objects path {knowledge_objects_path} does not exist"
    with open(knowledge_objects_path, "r", encoding="utf-8") as f:
        knowledge_objects = json.load(f)
    relevant_objects = [o for o in knowledge_objects if o["reference"] <= current_page]
    return sample(relevant_objects, limit)