"""Reader endpoints: serve PDFs, knowledge Q&A, mastery data."""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from paths import PDFS_PATH, OCR_PATH, KNOWLEDGE_OBJECTS_PATH
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

def _load_grouped_questions(book_name: str, page: int):
    """Load questions from grouped.json, filtered by page."""
    grouped_path = KNOWLEDGE_OBJECTS_PATH / book_name / "grouped.json"
    if not grouped_path.exists():
        return None

    with open(grouped_path, encoding="utf-8") as f:
        grouped = json.load(f)

    all_questions = []
    for cluster in grouped:
        refs = cluster.get("references", [])
        # Include cluster if any of its references are <= current page
        if any(r <= page for r in refs):
            for q in cluster["questions"]:
                all_questions.append({
                    "question": q,
                    "knowledge_object": cluster["cluster_name"],
                    "reference": min(refs),
                })
    return all_questions


def _load_raw_questions(book_name: str, page: int):
    """Load questions from raw versioned knowledge JSONs."""
    ko_path = _find_latest_ko(KNOWLEDGE_OBJECTS_PATH / book_name)
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

    # Check if grouped.json exists
    has_grouped = (KNOWLEDGE_OBJECTS_PATH / book_name / "grouped.json").exists()

    return {
        "name": book_name,
        "total_pages": len(data["pages"]),
        "has_grouped": has_grouped,
    }


@router.get("/books/{book_name:path}/knowledge")
async def get_knowledge(
    book_name: str,
    page: int = Query(0, ge=0),
    limit: int = Query(1, ge=1, le=20),
    mode: str = Query("grouped", regex="^(grouped|raw)$"),
):
    if mode == "grouped":
        all_questions = _load_grouped_questions(book_name, page)
        # Fallback to raw if grouped doesn't exist
        if all_questions is None:
            all_questions = _load_raw_questions(book_name, page)
    else:
        all_questions = _load_raw_questions(book_name, page)

    if not all_questions:
        return {"questions": [], "mode": mode}

    sampled = random.sample(all_questions, min(limit, len(all_questions)))
    return {"questions": sampled, "mode": mode}


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
