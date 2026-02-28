from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

from langfuse.langchain import CallbackHandler
from langchain_mistralai.chat_models import ChatMistralAI
from functools import cached_property


# Load .env from project root (new_backend/)
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
class Settings(BaseSettings):
    # Langfuse
    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_host: str | None = None

    # LLM
    llm_provider: str | None = None

    # Mistral AI
    mistral_api_key: str | None = None

    # Weights & Biases
    wandb_api_key: str | None = None

    # Internal parameters
    chunk_size: int | None = None
    stride: int | None = None

    @cached_property
    def langfuse_handler(self) -> CallbackHandler:
        return CallbackHandler()

    @property
    def llm_client(self):
        if self.llm_provider == "mistral":
            return ChatMistralAI(
                api_key=self.mistral_api_key,
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {self.llm_provider}")

settings = Settings()