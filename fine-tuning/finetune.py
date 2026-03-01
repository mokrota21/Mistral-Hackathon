"""
Fine-tune Mistral Small on the golden-standard training dataset using QLoRA.

Usage:
    uv run finetune.py
    uv run finetune.py --epochs 5 --lr 2e-4
    uv run finetune.py --model mistralai/Mistral-7B-Instruct-v0.3   # lighter model
"""

import argparse
import json
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer

from config import settings
from paths import DATA_PATH

TRAINING_DATA_PATH = DATA_PATH / "training_dataset.jsonl"
OUTPUT_DIR = DATA_PATH / "finetuned_model"
MODEL_ID = "mistralai/Mistral-Small-24B-Instruct-2501"


def load_dataset_from_jsonl(path: Path) -> Dataset:
    examples = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                examples.append(json.loads(line))
    return Dataset.from_list(examples)


def format_chat(example: dict, tokenizer) -> dict:
    """Apply the model's chat template so the trainer sees a single 'text' field."""
    text = tokenizer.apply_chat_template(
        example["messages"],
        tokenize=False,
        add_generation_prompt=False,
    )
    return {"text": text}


def main():
    parser = argparse.ArgumentParser(description="Fine-tune Mistral Small with QLoRA")
    parser.add_argument("--model", default=MODEL_ID)
    parser.add_argument("--data", default=str(TRAINING_DATA_PATH))
    parser.add_argument("--output", default=str(OUTPUT_DIR))
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--grad-accum", type=int, default=8)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--max-seq-len", type=int, default=4096)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument("--no-quantize", action="store_true",
                        help="Disable 4-bit quantization (needs much more VRAM)")
    parser.add_argument("--wandb-project", default="mistral-finetune")
    args = parser.parse_args()

    # ── 1. Tokenizer ────────────────────────────────────────────────
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

    # ── 2. Dataset ──────────────────────────────────────────────────
    dataset = load_dataset_from_jsonl(Path(args.data))
    dataset = dataset.map(
        lambda ex: format_chat(ex, tokenizer),
        remove_columns=dataset.column_names,
    )
    print(f"Training examples: {len(dataset)}")
    print(f"Sample (first 300 chars): {dataset[0]['text'][:300]}...")

    # ── 3. Model + optional 4-bit quantisation (QLoRA) ──────────────
    bnb_config = None
    if not args.no_quantize:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        quantization_config=bnb_config,
        device_map="auto",
        torch_dtype=torch.bfloat16,
        attn_implementation="eager",
    )
    model.config.use_cache = False

    if not args.no_quantize:
        model = prepare_model_for_kbit_training(model)

    # ── 4. LoRA adapters ────────────────────────────────────────────
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        bias="none",
        task_type=TaskType.CAUSAL_LM,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ── 5. Training arguments ───────────────────────────────────────
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()

    training_args = SFTConfig(
        output_dir=args.output,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_ratio=0.1,
        bf16=use_bf16,
        fp16=not use_bf16 and torch.cuda.is_available(),
        logging_steps=1,
        save_strategy="epoch",
        max_seq_length=args.max_seq_len,
        dataset_text_field="text",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        optim="paged_adamw_8bit" if not args.no_quantize else "adamw_torch",
        report_to="wandb" if settings.wandb_api_key else "none",
        run_name="mistral-small-finetune",
    )

    # ── 6. Train ────────────────────────────────────────────────────
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
    )

    print("Starting training...")
    trainer.train()

    # ── 7. Save adapter weights ─────────────────────────────────────
    trainer.save_model(args.output)
    tokenizer.save_pretrained(args.output)
    print(f"\nAdapter weights saved to {args.output}")
    print(f"To load later:\n"
          f"  from peft import AutoPeftModelForCausalLM\n"
          f"  model = AutoPeftModelForCausalLM.from_pretrained('{args.output}')")


if __name__ == "__main__":
    main()
