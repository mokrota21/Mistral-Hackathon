from abc import ABC, abstractmethod
from typing import List, Dict, Any
import re
from config import settings
from paths import CHUNKS_PATH, OCR_PATH
from pathlib import Path
import json
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    force=True,
)
logger = logging.getLogger(__name__)

class Chunker(ABC):
    def __init__(self) -> None:
        self.name="UndefinedChunker"

    @abstractmethod
    def chunk(self, pages_text: List[str]) -> List[Dict[str, Any]]:
        """
        Chunks pages texts. Returns list of chunks.
        """
        pass

class SimpleChunker(Chunker):
    def __init__(self, chunk_size: int = settings.chunk_size, stride: int = settings.stride) -> None:
        super().__init__()
        self.chunk_size = chunk_size
        self.stride = stride
        self.name="SimpleChunker"

    def chunk(self, pages_text: List[str], page_numbers: List[int]) -> List[Dict[str, Any]]:
        chunks = []
        buffer = ""
        for page_num, page_text in zip(page_numbers, pages_text):
            buffer += page_text
            while len(buffer) >= self.chunk_size:
                chunks.append(
                    {
                        "text": buffer[:self.chunk_size],
                        "page_no": page_num
                    }
                )
                buffer = buffer[self.stride:]
                
        if buffer:
            chunks.append(
                {
                    "text": buffer,
                    "page_no": page_num,
                }
            )
        return chunks

DefaultChunker = SimpleChunker
chunker = DefaultChunker()

def chunk_textbook(textbook_name: str) -> None:
    """
    Chunks the textbook into chunks.
    """
    ocr_path = OCR_PATH / f"{textbook_name}.json"
    assert ocr_path.exists(), f"OCR path {ocr_path} does not exist"
    with open(ocr_path, "r", encoding="utf-8") as f:
        ocr_data = json.load(f)

    page_texts = [p["markdown"] for p in ocr_data["pages"]]
    page_numbers = [p["index"] for p in ocr_data["pages"]]
    chunks = chunker.chunk(page_texts, page_numbers)
    with open(CHUNKS_PATH / f"{textbook_name}.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=4)
    logger.info(f"Textbook {textbook_name} chunked into {len(chunks)} chunks")