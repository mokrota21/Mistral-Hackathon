"""Library endpoints: list books, upload, status, rerun stages."""

from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from pydantic import BaseModel
from paths import PDFS_PATH
from services.processing import (
    book_statuses, BookInfo, BookStatus, run_pipeline,
    run_single_stage, STAGES, AVAILABLE_PROVIDERS, _get_default_provider,
)

router = APIRouter(tags=["library"])


@router.get("/books")
async def list_books():
    return {"books": [info.to_dict() for info in book_statuses.values()]}


@router.post("/books/upload")
async def upload_book(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(400, "Only PDF files are accepted")

    filename = file.filename

    if filename in book_statuses:
        raise HTTPException(409, f"Book '{filename}' already exists")

    # Save PDF to disk
    pdf_path = PDFS_PATH / filename
    contents = await file.read()
    with open(pdf_path, "wb") as f:
        f.write(contents)

    # Initialize status
    book_statuses[filename] = BookInfo(
        name=filename, status=BookStatus.OCR_PROCESSING
    )

    # Start background pipeline (sync function → runs in threadpool)
    background_tasks.add_task(run_pipeline, filename)

    return {
        "name": filename,
        "status": "ocr_processing",
        "message": "Processing started",
    }


class RerunStageRequest(BaseModel):
    stage: str
    provider: str = "mistral"


@router.post("/books/{book_name:path}/rerun-stage")
async def rerun_stage(
    book_name: str,
    body: RerunStageRequest,
    background_tasks: BackgroundTasks,
):
    """Rerun a single pipeline stage for a book."""
    if book_name not in book_statuses:
        raise HTTPException(404, f"Book '{book_name}' not found")

    if body.stage not in STAGES:
        raise HTTPException(400, f"Unknown stage '{body.stage}'. Valid: {STAGES}")

    current_status = book_statuses[book_name].status
    busy = (BookStatus.OCR_PROCESSING, BookStatus.CHUNKING, BookStatus.ANALYZING, BookStatus.RERUNNING)
    if current_status in busy:
        raise HTTPException(409, f"Book is currently being processed ({current_status.value})")

    background_tasks.add_task(run_single_stage, book_name, body.stage, body.provider)

    return {
        "name": book_name,
        "stage": body.stage,
        "provider": body.provider,
        "status": "rerunning",
        "message": f"Stage '{body.stage}' started (provider={body.provider})",
    }


@router.get("/books/stages")
async def get_stages():
    """Return available pipeline stages and providers."""
    return {
        "stages": STAGES,
        "providers": AVAILABLE_PROVIDERS,
        "default_provider": _get_default_provider(),
    }


@router.get("/books/{book_name:path}/status")
async def book_status(book_name: str):
    if book_name not in book_statuses:
        raise HTTPException(404, f"Book '{book_name}' not found")
    return book_statuses[book_name].to_dict()
