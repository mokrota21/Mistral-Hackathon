"""Library endpoints: list books, upload, status."""

from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from paths import PDFS_PATH
from services.processing import book_statuses, BookInfo, BookStatus, run_pipeline

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


@router.get("/books/{book_name:path}/status")
async def book_status(book_name: str):
    if book_name not in book_statuses:
        raise HTTPException(404, f"Book '{book_name}' not found")
    return book_statuses[book_name].to_dict()
