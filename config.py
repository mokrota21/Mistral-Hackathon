from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from langfuse.langchain import CallbackHandler
from langchain_mistralai.chat_models import ChatMistralAI
from functools import cached_property
from mistralai import Mistral

_env_path = Path(__file__).resolve().parent / ".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(_env_path),
        env_file_encoding="utf-8-sig",
        extra="ignore",
    )

    # Langfuse
    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_host: str | None = None

    # LLM
    llm_provider: str | None = None
    finetune_service_url: str = "http://localhost:8001/v1"

    # Mistral AI
    mistral_api_key: str | None = None

    # Weights & Biases
    wandb_api_key: str | None = None

    # Internal parameters
    chunk_size: int | None = None
    stride: int | None = None
    similarity_threshold: float = 0.99

    @cached_property
    def langfuse_handler(self) -> CallbackHandler:
        return CallbackHandler()

    @property
    def llm_client(self):
        return self.get_llm_client(self.llm_provider)

    def get_llm_client(self, provider: str = None):
        """Return LLM client for the given provider name."""
        provider = provider or self.llm_provider
        if provider == "mistral":
            return ChatMistralAI(
                api_key=self.mistral_api_key,
            )
        elif provider == "fine-tuned":
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(
                base_url=self.finetune_service_url,
                api_key="dummy",
                model="local",
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

    @property
    def teacher_llm_client(self):
        return ChatMistralAI(
            model="mistral-large-latest",
            api_key=self.mistral_api_key,
        )

    @property
    def mistral_client(self):
        client = Mistral(api_key=self.mistral_api_key)
        return client

settings = Settings()