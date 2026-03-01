"""Background pipeline orchestrator + in-memory status tracking."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional
import json
import logging

from paths import PDFS_PATH, OCR_PATH, CHUNKS_PATH, KNOWLEDGE_OBJECTS_PATH

logger = logging.getLogger(__name__)


AVAILABLE_PROVIDERS = ["mistral", "fine-tuned"]


def _get_default_provider() -> str:
    """Return the default LLM provider from config, or 'mistral' if unset."""
    from config import settings
    return settings.llm_provider or "mistral"


def _find_latest_ko(ko_dir):
    """Return path to the latest versioned knowledge JSON, or None."""
    if not ko_dir.exists():
        return None
    existing = [f for f in ko_dir.glob("*.json") if f.stem.isdigit()]
    if not existing:
        return None
    return max(existing, key=lambda f: int(f.stem))


class BookStatus(str, Enum):
    UPLOADING = "uploading"
    OCR_PROCESSING = "ocr_processing"
    CHUNKING = "chunking"
    ANALYZING = "analyzing"
    RERUNNING = "rerunning"
    READY = "ready"
    ERROR = "error"


@dataclass
class BookInfo:
    name: str
    status: BookStatus
    total_pages: Optional[int] = None
    total_knowledge_objects: Optional[int] = None
    error_message: Optional[str] = None

    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status.value,
            "total_pages": self.total_pages,
            "total_knowledge_objects": self.total_knowledge_objects,
            "error_message": self.error_message,
        }


# ── In-memory status store ──
book_statuses: Dict[str, BookInfo] = {}


def _get_book_providers(book_name: str):
    """Return list of provider names that have knowledge data for a book."""
    book_ko_dir = KNOWLEDGE_OBJECTS_PATH / book_name
    if not book_ko_dir.exists():
        return []
    return [
        d.name for d in book_ko_dir.iterdir()
        if d.is_dir() and _find_latest_ko(d) is not None
    ]


def init_book_statuses():
    """Scan data directories on startup to build initial status map."""
    PDFS_PATH.mkdir(parents=True, exist_ok=True)
    OCR_PATH.mkdir(parents=True, exist_ok=True)
    CHUNKS_PATH.mkdir(parents=True, exist_ok=True)
    KNOWLEDGE_OBJECTS_PATH.mkdir(parents=True, exist_ok=True)

    for pdf_file in PDFS_PATH.glob("*.pdf"):
        name = pdf_file.name
        info = BookInfo(name=name, status=BookStatus.READY)

        ocr_path = OCR_PATH / f"{name}.json"
        chunks_path = CHUNKS_PATH / f"{name}.json"

        # Check for knowledge across all provider subdirectories
        providers_with_data = _get_book_providers(name)

        if ocr_path.exists():
            try:
                with open(ocr_path, encoding="utf-8") as f:
                    ocr_data = json.load(f)
                info.total_pages = len(ocr_data.get("pages", []))
            except Exception:
                pass

        # Count knowledge objects across all providers
        total_ko = 0
        for prov in providers_with_data:
            ko_latest = _find_latest_ko(KNOWLEDGE_OBJECTS_PATH / name / prov)
            if ko_latest:
                try:
                    with open(ko_latest, encoding="utf-8") as f:
                        ko_data = json.load(f)
                    total_ko += sum(
                        len(entry.get("knowledge_objects", []))
                        for entry in ko_data
                    )
                except Exception:
                    pass
        if total_ko > 0:
            info.total_knowledge_objects = total_ko

        # Determine actual status based on what data exists
        if not ocr_path.exists():
            info.status = BookStatus.ERROR
            info.error_message = "OCR data missing — re-upload to process"
        elif not chunks_path.exists():
            info.status = BookStatus.ERROR
            info.error_message = "Chunks missing — re-upload to process"
        elif not providers_with_data:
            info.status = BookStatus.ERROR
            info.error_message = "Knowledge extraction incomplete — re-upload to process"
        else:
            info.status = BookStatus.READY

        book_statuses[name] = info

    logger.info(f"Initialized {len(book_statuses)} book(s) from data directory")


def run_pipeline(book_name: str, provider: str = None):
    """
    Synchronous background task: run OCR -> chunk -> analyze pipeline.

    Called by FastAPI BackgroundTasks which runs sync functions in a threadpool,
    so asyncio.run() inside analyze_textbook will work fine (new event loop in thread).
    """
    if provider is None:
        provider = _get_default_provider()

    try:
        pdf_path = PDFS_PATH / book_name

        # Stage 1: OCR
        logger.info(f"[{book_name}] Starting OCR...")
        book_statuses[book_name].status = BookStatus.OCR_PROCESSING
        from ocr_service import process_textbook
        process_textbook(str(pdf_path))

        # Update page count
        ocr_path = OCR_PATH / f"{book_name}.json"
        with open(ocr_path, encoding="utf-8") as f:
            ocr_data = json.load(f)
        book_statuses[book_name].total_pages = len(ocr_data["pages"])
        logger.info(f"[{book_name}] OCR complete: {book_statuses[book_name].total_pages} pages")

        # Stage 2: Chunking
        logger.info(f"[{book_name}] Starting chunking...")
        book_statuses[book_name].status = BookStatus.CHUNKING
        from chunks_service import chunk_textbook
        chunk_textbook(book_name)
        logger.info(f"[{book_name}] Chunking complete")

        # Stage 3–5: Knowledge extraction → embedding → grouping
        _run_knowledge_stages(book_name, provider)

        book_statuses[book_name].status = BookStatus.READY
        logger.info(f"[{book_name}] Pipeline complete! {book_statuses[book_name].total_knowledge_objects} knowledge objects")

    except Exception as e:
        logger.error(f"[{book_name}] Pipeline error: {e}", exc_info=True)
        book_statuses[book_name].status = BookStatus.ERROR
        book_statuses[book_name].error_message = str(e)


def _run_knowledge_stages(book_name: str, provider: str):
    """Stages 3–5: knowledge extraction, embedding, grouping (shared by full pipeline & rerun)."""
    # Stage 3: Knowledge extraction
    logger.info(f"[{book_name}] Starting knowledge extraction (provider={provider})...")
    book_statuses[book_name].status = BookStatus.ANALYZING
    from knowledge_service import analyze_textbook
    analyze_textbook(book_name, limit=9999, provider=provider)

    # Stage 4: Embedding
    logger.info(f"[{book_name}] Starting embedding (provider={provider})...")
    from embed_service import embed_textbook
    embed_textbook(book_name, provider=provider)
    logger.info(f"[{book_name}] Embedding complete")

    # Stage 5: Clustering / grouping
    logger.info(f"[{book_name}] Starting knowledge grouping (provider={provider})...")
    from embed_service import merge_knowledge
    merge_knowledge(book_name, provider=provider)
    logger.info(f"[{book_name}] Knowledge grouping complete")

    # Update knowledge count
    ko_latest = _find_latest_ko(KNOWLEDGE_OBJECTS_PATH / book_name / provider)
    if ko_latest:
        with open(ko_latest, encoding="utf-8") as f:
            ko_data = json.load(f)
        book_statuses[book_name].total_knowledge_objects = sum(
            len(e.get("knowledge_objects", [])) for e in ko_data
        )


def run_knowledge_pipeline(book_name: str, provider: str):
    """
    Rerun only knowledge extraction + embedding + grouping (stages 3–5).
    Assumes OCR and chunking already exist. Used by the "Rerun" button.
    """
    try:
        book_statuses[book_name].status = BookStatus.RERUNNING
        book_statuses[book_name].error_message = None

        _run_knowledge_stages(book_name, provider)

        book_statuses[book_name].status = BookStatus.READY
        logger.info(f"[{book_name}] Knowledge rerun complete (provider={provider})!")

    except Exception as e:
        logger.error(f"[{book_name}] Knowledge rerun error: {e}", exc_info=True)
        book_statuses[book_name].status = BookStatus.ERROR
        book_statuses[book_name].error_message = str(e)
