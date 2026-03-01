from config import settings
from base64 import b64encode
import json
from paths import OCR_PATH
from pathlib import Path
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

def encode_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        return b64encode(pdf_file.read()).decode('utf-8')

class OcrService:
    def __init__(self) -> None:
        self.ocr_model = settings.ocr_client

    def process(self, file_path: str, output_path: str) -> str:
        base64_pdf = encode_pdf(file_path)
        response = self.ocr_model.ocr.process(
            model="mistral-ocr-latest",
            document = {
                "type": "document_url",
                "document_url": f"data:application/pdf;base64,{base64_pdf}" 
            },
            table_format="markdown",
            include_image_base64=True,
        )
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(response.model_dump(), indent=4))

ocr_service = OcrService()

def process_textbook(textbook_path: str) -> str:
    textbook_path = Path(textbook_path)
    textbook_name = textbook_path.name
    logger.info(f"Processing textbook: {textbook_name}")
    ocr_service.process(textbook_path, OCR_PATH / f"{textbook_name}.json")
    logger.info(f"Textbook processed: {textbook_name}")

if __name__ == "__main__":
    ocr_service = OcrService()
    path = r"C:\Users\mokrota\Downloads\Erbol Esengulov - Appendix Antecedents Certificate.pdf"
    ocr_service.process(path, "output.json")