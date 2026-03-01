"""AInki - FastAPI web application."""

import logging
import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.library import router as library_router
from api.reader import router as reader_router
from services.processing import init_book_statuses

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    force=True,
)
logger = logging.getLogger(__name__)

STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: scan existing data
    init_book_statuses()
    logger.info("AInki server ready")
    yield
    # Shutdown
    logger.info("AInki server shutting down")


app = FastAPI(
    title="AInki",
    description="Read. Retain. Remember.",
    version="0.1.0",
    lifespan=lifespan,
)

# ── API routes ──
app.include_router(library_router, prefix="/api")
app.include_router(reader_router, prefix="/api")

# ── Static assets (CSS, JS) ──
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# ── HTML page routes ──
@app.get("/")
async def library_page():
    return FileResponse(STATIC_DIR / "library.html")


@app.get("/reader/{book_name:path}")
async def reader_page(book_name: str):
    return FileResponse(STATIC_DIR / "reader.html")
