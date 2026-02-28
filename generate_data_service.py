from pathlib import Path
from chunks_service import DefaultChunker
from llm_agent import analyze_chunk
from asyncio import run, gather

TEXTBOOK_PATH = Path(__file__).parent / "Introduction to Probability by Joseph K. Blitzstein, Jessica Hwang (z-lib.org).pdf" / "markdown.md"
with open(TEXTBOOK_PATH, encoding="utf-8", mode="r") as file:
    textbook_text = file.read()
chunker = DefaultChunker()



if __name__ == "__main__":
    chunks = [c["text"] for c in chunker.chunk([textbook_text])]
    knowledge = run(analyze_chunk(chunks[0]))
    with open("knowledge.json", encoding="utf-8", mode="w") as file:
        file.write(knowledge.model_dump_json(indent=4))