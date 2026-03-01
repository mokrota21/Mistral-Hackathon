"""
Fine-tune mistral-small-latest via the Mistral API (cloud-based, no GPU needed).

Usage:
    uv run finetune_api.py                              # upload + create + start job
    uv run finetune_api.py --training-steps 20 --lr 1e-4
    uv run finetune_api.py --status JOB_ID              # check job status
    uv run finetune_api.py --test JOB_ID                # test the fine-tuned model
"""

import argparse
import time

from mistralai import Mistral
from mistralai.models import WandbIntegration

from config import settings
from paths import DATA_PATH

TRAINING_DATA_PATH = DATA_PATH / "training_dataset_filtered.jsonl"


def upload_file(client: Mistral, path: str) -> str:
    with open(path, "rb") as f:
        uploaded = client.files.upload(file={"file_name": path, "content": f})
    print(f"Uploaded {path}  ->  file_id={uploaded.id}")
    return uploaded.id


def create_and_start_job(
    client: Mistral,
    training_file_id: str,
    model: str,
    training_steps: int,
    learning_rate: float,
    wandb_project: str | None,
    suffix: str | None,
) -> str:
    integrations = None
    if settings.wandb_api_key and wandb_project:
        integrations = [
            WandbIntegration(
                project=wandb_project,
                run_name=suffix or "ainki-finetune",
                api_key=settings.wandb_api_key,
            )
        ]

    job = client.fine_tuning.jobs.create(
        model=model,
        training_files=[{"file_id": training_file_id, "weight": 1}],
        hyperparameters={
            "training_steps": training_steps,
            "learning_rate": learning_rate,
        },
        auto_start=True,
        suffix=suffix,
        integrations=integrations,
    )
    print(f"Fine-tuning job created: {job.id}")
    print(f"  model:          {model}")
    print(f"  training_steps: {training_steps}")
    print(f"  learning_rate:  {learning_rate}")
    print(f"  status:         {job.status}")
    return job.id


def poll_until_done(client: Mistral, job_id: str, poll_interval: int = 30):
    print(f"\nPolling job {job_id} every {poll_interval}s ...")
    while True:
        job = client.fine_tuning.jobs.get(job_id=job_id)
        status = job.status
        print(f"  status: {status}")

        if status in ("SUCCESS", "FAILED", "FAILED_VALIDATION", "CANCELLED"):
            if status == "SUCCESS":
                print(f"\nDone! Fine-tuned model name: {job.fine_tuned_model}")
                print(f"Use it in the API with:  model=\"{job.fine_tuned_model}\"")
            else:
                print(f"\nJob ended with status: {status}")
            return job

        time.sleep(poll_interval)


def check_status(client: Mistral, job_id: str):
    job = client.fine_tuning.jobs.get(job_id=job_id)
    print(f"Job ID:            {job.id}")
    print(f"Status:            {job.status}")
    print(f"Model:             {job.model}")
    if job.fine_tuned_model:
        print(f"Fine-tuned model:  {job.fine_tuned_model}")
    return job


def test_model(client: Mistral, job_id: str, prompt: str):
    job = client.fine_tuning.jobs.get(job_id=job_id)
    if job.status != "SUCCESS":
        print(f"Job status is {job.status}, not SUCCESS. Cannot test yet.")
        return
    model_name = job.fine_tuned_model
    print(f"Testing model: {model_name}\n")

    response = client.chat.complete(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are an expert at analyzing educational content and extracting important knowledge that students should remember."},
            {"role": "user", "content": prompt},
        ],
    )
    print(response.choices[0].message.content)


def main():
    parser = argparse.ArgumentParser(description="Fine-tune Mistral Small via the Mistral API")
    parser.add_argument("--model", default="mistral-small-latest",
                        help="API model name to fine-tune")
    parser.add_argument("--data", default=str(TRAINING_DATA_PATH))
    parser.add_argument("--training-steps", type=int, default=10)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--suffix", default=None,
                        help="Suffix appended to the fine-tuned model name")
    parser.add_argument("--wandb-project", default="mistral-finetune")
    parser.add_argument("--no-poll", action="store_true",
                        help="Don't wait for the job to finish")
    parser.add_argument("--status", metavar="JOB_ID",
                        help="Check status of an existing job (skip training)")
    parser.add_argument("--test", metavar="JOB_ID",
                        help="Test a completed fine-tuned model")
    parser.add_argument("--test-prompt", default="Explain what probability is and why it matters.",
                        help="Prompt used with --test")
    args = parser.parse_args()
    
    client = Mistral(api_key=settings.mistral_api_key)

    if args.status:
        check_status(client, args.status)
        return

    if args.test:
        test_model(client, args.test, args.test_prompt)
        return

    # ── 1. Upload training data ─────────────────────────────────────
    print(f"Uploading {args.data} ...")
    file_id = upload_file(client, args.data)

    # ── 2. Create fine-tuning job ───────────────────────────────────
    job_id = create_and_start_job(
        client,
        training_file_id=file_id,
        model=args.model,
        training_steps=args.training_steps,
        learning_rate=args.lr,
        wandb_project=args.wandb_project,
        suffix=args.suffix,
    )

    # ── 3. Poll until done ──────────────────────────────────────────
    if not args.no_poll:
        poll_until_done(client, job_id)
    else:
        print(f"\nJob {job_id} submitted. Check later with:")
        print(f"  uv run finetune_api.py --status {job_id}")


if __name__ == "__main__":
    main()
