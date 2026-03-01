"""
Local server for the fine-tuned Mistral LoRA adapter.
Exposes an OpenAI-compatible POST /v1/chat/completions so the main app
can use it via LangChain's ChatOpenAI(base_url=...).

Run separately (requires torch, transformers, peft):
  uv run finetune_service.py
  # or with optional deps: uv sync --group finetune && uv run finetune_service.py

Set in .env:
  LLM_PROVIDER=fine-tuned
  FINETUNE_SERVICE_URL=http://localhost:8001/v1
"""
from __future__ import annotations

import logging
import os
import uuid
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("finetune_service")

app = FastAPI(title="AInki Fine-tuned Model", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    """OpenAI-compatible request body.

    LangChain may send extra fields (tools, response_format, etc.)
    that this local server doesn't support — we explicitly allow
    and ignore them via model_config.
    """
    model_config = {"extra": "ignore"}

    model: str = "local"
    messages: list[ChatMessage]
    stream: bool = False
    max_tokens: int | None = 1024
    temperature: float = 0.7


def _get_model_and_tokenizer():
    """Load base model + LoRA adapter once; reuse."""
    if _get_model_and_tokenizer._model is not None:
        return _get_model_and_tokenizer._model, _get_model_and_tokenizer._tokenizer
    try:
        import torch
        from transformers import AutoTokenizer, BitsAndBytesConfig
        from peft import AutoPeftModelForCausalLM
    except ImportError as e:
        raise RuntimeError(
            "Fine-tune service requires torch, transformers, peft, bitsandbytes. "
            "Install with: uv add torch transformers peft accelerate bitsandbytes"
        ) from e

    adapter_path = os.environ.get(
        "FINETUNED_MODEL_PATH",
        str(Path(__file__).resolve().parent / "data" / "kaggle" / "finetuned_model"),
    )
    adapter_path = Path(adapter_path)
    if not adapter_path.exists():
        raise FileNotFoundError(f"Fine-tuned adapter path not found: {adapter_path}")

    logger.info("Loading tokenizer from %s", adapter_path)
    tokenizer = AutoTokenizer.from_pretrained(adapter_path, trust_remote_code=True)

    # Mistral-7B bf16 needs ~14GB VRAM.  Use 4-bit quantization so it fits
    # comfortably in 8GB cards (RTX 3060 Ti, etc.).
    use_4bit = torch.cuda.is_available() and (
        torch.cuda.get_device_properties(0).total_memory < 12 * 1024**3  # < 12 GB
    )
    quant_config = None
    if use_4bit:
        logger.info("GPU VRAM < 12 GB — loading model in 4-bit (NF4) quantization")
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

    logger.info("Loading base model + PEFT adapter...")
    device_map = "auto" if use_4bit else ("cuda:0" if torch.cuda.is_available() else "cpu")
    model = AutoPeftModelForCausalLM.from_pretrained(
        adapter_path,
        device_map=device_map,
        quantization_config=quant_config,
        dtype=torch.bfloat16,
        trust_remote_code=True,
        token=os.environ.get("HF_TOKEN"),
    )
    model.eval()
    _get_model_and_tokenizer._model = model
    _get_model_and_tokenizer._tokenizer = tokenizer
    return model, tokenizer


_get_model_and_tokenizer._model = None
_get_model_and_tokenizer._tokenizer = None


def _messages_to_prompt(messages: list[dict], tokenizer) -> str:
    """Turn OpenAI-style messages into a single prompt using the model's chat template."""
    if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        return prompt
    parts = []
    for m in messages:
        role, content = m.get("role", "user"), m.get("content", "")
        parts.append(f"<{role}>\n{content}")
    parts.append("<assistant>\n")
    return "\n".join(parts)


@app.post("/v1/chat/completions")
def chat_completions(body: ChatCompletionRequest):
    if body.stream:
        raise HTTPException(status_code=400, detail="Streaming not implemented")
    try:
        model, tokenizer = _get_model_and_tokenizer()
    except Exception as e:
        logger.exception("Model load failed")
        raise HTTPException(status_code=503, detail=str(e)) from e

    messages = [{"role": m.role, "content": m.content} for m in body.messages]
    prompt = _messages_to_prompt(messages, tokenizer)
    max_new_tokens = body.max_tokens or 1024

    try:
        import torch
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=body.temperature,
                do_sample=body.temperature > 0,
                pad_token_id=tokenizer.eos_token_id,
            )
        generated = tokenizer.decode(out[0][inputs.input_ids.shape[1] :], skip_special_tokens=True)
    except Exception as e:
        logger.exception("Generate failed")
        raise HTTPException(status_code=500, detail=str(e)) from e

    return {
        "id": f"chatcmpl-{uuid.uuid4().hex[:24]}",
        "object": "chat.completion",
        "model": body.model,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": generated.strip()},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": int(inputs.input_ids.numel()),
            "completion_tokens": out.shape[1] - inputs.input_ids.shape[1],
            "total_tokens": out.shape[1],
        },
    }


@app.get("/health")
def health():
    return {"status": "ok"}


def main():
    import uvicorn
    port = int(os.environ.get("FINETUNE_SERVICE_PORT", "8001"))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
