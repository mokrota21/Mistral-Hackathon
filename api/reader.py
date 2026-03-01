"""Reader endpoints: serve PDFs, knowledge Q&A, mastery data."""

from fastapi import APIRouter, BackgroundTasks, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from paths import PDFS_PATH, OCR_PATH, KNOWLEDGE_OBJECTS_PATH
from services.processing import AVAILABLE_PROVIDERS, _get_default_provider
import json
import random

router = APIRouter(tags=["reader"])


def _find_latest_ko(ko_dir):
    """Return path to the latest versioned knowledge JSON, or None."""
    if not ko_dir.exists():
        return None
    existing = [f for f in ko_dir.glob("*.json") if f.stem.isdigit()]
    if not existing:
        return None
    return max(existing, key=lambda f: int(f.stem))


# ── Schemas ──

class AnswerSubmission(BaseModel):
    question: str
    knowledge_object: str
    user_answer: str
    page: int = 0


# ── Knowledge helpers ──

def _load_grouped_clusters(book_name: str, page: int, provider: str):
    """Load clusters from grouped.json, filtered by page. Returns cluster-level data."""
    grouped_path = KNOWLEDGE_OBJECTS_PATH / book_name / provider / "grouped.json"
    if not grouped_path.exists():
        return None

    with open(grouped_path, encoding="utf-8") as f:
        grouped = json.load(f)

    clusters = []
    for cluster in grouped:
        refs = cluster.get("references", [])
        # Include cluster if any of its references are <= current page
        if any(r <= page for r in refs):
            clusters.append({
                "cluster_name": cluster["cluster_name"],
                "questions": cluster["questions"],
                "question_count": len(cluster["questions"]),
                "references": refs,
            })
    return clusters


def _load_raw_questions(book_name: str, page: int, provider: str):
    """Load questions from raw versioned knowledge JSONs."""
    ko_path = _find_latest_ko(KNOWLEDGE_OBJECTS_PATH / book_name / provider)
    if ko_path is None:
        return None

    with open(ko_path, encoding="utf-8") as f:
        knowledge_objects = json.load(f)

    all_questions = []
    for chunk_ko in knowledge_objects:
        if chunk_ko.get("reference", 0) <= page:
            for ko in chunk_ko.get("knowledge_objects", []):
                all_questions.append({
                    "question": ko["question"],
                    "knowledge_object": ko["knowledge_object"],
                    "reference": chunk_ko["reference"],
                })
    return all_questions


def _get_book_providers(book_name: str):
    """Return list of providers that have knowledge data for this book."""
    book_dir = KNOWLEDGE_OBJECTS_PATH / book_name
    if not book_dir.exists():
        return []
    return [
        d.name for d in book_dir.iterdir()
        if d.is_dir() and _find_latest_ko(d) is not None
    ]


# ── Endpoints ──

@router.get("/pdfs/{book_name:path}")
async def serve_pdf(book_name: str):
    pdf_path = PDFS_PATH / book_name
    if not pdf_path.exists():
        raise HTTPException(404, "PDF not found")
    return FileResponse(pdf_path, media_type="application/pdf")


@router.get("/books/{book_name:path}/pages")
async def book_pages(book_name: str):
    ocr_path = OCR_PATH / f"{book_name}.json"
    if not ocr_path.exists():
        raise HTTPException(404, "Book OCR data not found")
    with open(ocr_path, encoding="utf-8") as f:
        data = json.load(f)

    # Gather provider info
    providers_with_data = _get_book_providers(book_name)
    default_provider = _get_default_provider()

    # Build per-provider grouped status
    provider_info = {}
    for prov in providers_with_data:
        has_grouped = (KNOWLEDGE_OBJECTS_PATH / book_name / prov / "grouped.json").exists()
        provider_info[prov] = {"has_grouped": has_grouped}

    return {
        "name": book_name,
        "total_pages": len(data["pages"]),
        "available_providers": AVAILABLE_PROVIDERS,
        "providers_with_data": providers_with_data,
        "provider_info": provider_info,
        "default_provider": default_provider,
    }


@router.get("/books/{book_name:path}/knowledge")
async def get_knowledge(
    book_name: str,
    page: int = Query(0, ge=0),
    limit: int = Query(1, ge=1, le=50),
    mode: str = Query("grouped", regex="^(grouped|raw)$"),
    provider: str = Query(None),
):
    if provider is None:
        provider = _get_default_provider()

    if mode == "grouped":
        clusters = _load_grouped_clusters(book_name, page, provider)
        if clusters is not None:
            sampled = random.sample(clusters, min(limit, len(clusters)))
            return {"clusters": sampled, "questions": [], "mode": "grouped", "provider": provider}
        # Fallback to raw if grouped doesn't exist
        mode = "raw"

    # Raw mode: return individual questions
    all_questions = _load_raw_questions(book_name, page, provider)

    if not all_questions:
        return {"clusters": [], "questions": [], "mode": mode, "provider": provider}

    sampled = random.sample(all_questions, min(limit, len(all_questions)))
    return {"clusters": [], "questions": sampled, "mode": mode, "provider": provider}


class RerunRequest(BaseModel):
    provider: str = "mistral"


@router.post("/books/{book_name:path}/rerun")
async def rerun_knowledge(
    book_name: str,
    body: RerunRequest,
    background_tasks: BackgroundTasks,
):
    """Rerun knowledge extraction + embedding + grouping for a specific provider."""
    from services.processing import book_statuses, BookStatus, run_knowledge_pipeline
    from paths import CHUNKS_PATH

    if book_name not in book_statuses:
        raise HTTPException(404, f"Book '{book_name}' not found")

    current_status = book_statuses[book_name].status
    if current_status in (BookStatus.OCR_PROCESSING, BookStatus.CHUNKING, BookStatus.ANALYZING, BookStatus.RERUNNING):
        raise HTTPException(409, f"Book is currently being processed ({current_status.value})")

    chunks_path = CHUNKS_PATH / f"{book_name}.json"
    if not chunks_path.exists():
        raise HTTPException(400, "Chunks not available — run full pipeline first")

    background_tasks.add_task(run_knowledge_pipeline, book_name, body.provider)

    return {
        "name": book_name,
        "provider": body.provider,
        "status": "rerunning",
        "message": f"Knowledge extraction rerun started with provider={body.provider}",
    }


@router.post("/books/{book_name:path}/answers")
async def submit_answer(book_name: str, answer: AnswerSubmission):
    # Dummy implementation - just acknowledge
    # Future: store in DB, evaluate with LLM
    return {
        "status": "stored",
        "feedback": "Thank you for your answer! Your response has been recorded.",
    }


@router.get("/books/{book_name:path}/mastery")
async def get_mastery(book_name: str):
    ocr_path = OCR_PATH / f"{book_name}.json"
    if not ocr_path.exists():
        raise HTTPException(404, "Book OCR data not found")

    with open(ocr_path, encoding="utf-8") as f:
        data = json.load(f)
    total = len(data["pages"])

    # Dummy mastery data - seeded by book name for consistency
    rng = random.Random(book_name)
    mastery = []
    for i in range(total):
        score = round(rng.uniform(0.15, 1.0), 2)
        if score > 0.7:
            status = "strong"
        elif score > 0.4:
            status = "moderate"
        else:
            status = "weak"
        mastery.append({"page": i, "score": score, "status": status})

    return {"total_pages": total, "mastery": mastery}
