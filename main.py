from ocr_service import process_textbook
from chunks_service import chunk_textbook
from knowledge_service import analyze_textbook, fetch_relevant_knowledge

import logging
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    force=True,
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting the main function")
    textbook_path = r"C:\torrent\Introduction to Probability by Joseph K. Blitzstein, Jessica Hwang (z-lib.org) (1).pdf"
    textbook_name = Path(textbook_path).name
    process_textbook(textbook_path)
    chunk_textbook(textbook_name)
    analyze_textbook(textbook_name)
    relevant_knowledge = fetch_relevant_knowledge(textbook_name, limit=1)
    logger.info(f"Relevant knowledge: {relevant_knowledge}")


if __name__ == "__main__":
    main()