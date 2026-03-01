from config import settings
import logging
import sys
from paths import KNOWLEDGE_OBJECTS_PATH
import json
from typing import List, Any
from sklearn.metrics.pairwise import euclidean_distances


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    force=True,
)
logger = logging.getLogger(__name__)

def embed_text(texts: List[str]) -> Any:
    response = settings.mistral_client.embeddings.create(
        model="mistral-embed",
        inputs=texts,
    )
    return [d.embedding for d in response.data]

def embed_textbook(textbook_name: str) -> None:
    knowledge_objects_path = KNOWLEDGE_OBJECTS_PATH / textbook_name
    knowledge_files = [
        p for p in knowledge_objects_path.glob("*.json")
        if p.name != "all_embeddings.json"
    ]
    knowledge_objects = []
    for knowledge_file in knowledge_files:
        with open(knowledge_file, "r", encoding="utf-8") as f:
            raw = f.read().strip()
            if not raw:
                logger.warning(f"Skipping empty file: {knowledge_file}")
                continue
            knowledge_objects.extend(json.loads(raw))

    for k in knowledge_objects:
        questions = [k_item["question"] for k_item in k["knowledge_objects"]]
        embedding = embed_text(questions)
        for id, e in enumerate(embedding):
            k["knowledge_objects"][id]["embedding"] = e
    
    save_path = knowledge_objects_path / f"all_embeddings.json"
    logger.info(f"Saving embeddings of {textbook_name} to {save_path} ...")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(knowledge_objects, f, indent=4)
    logger.info(f"Embeddings of {textbook_name} saved")

def merge_knowledge(textbook_name: str) -> None:
    """
    Cluster knowledge objects by cosine similarity of their question embeddings.
    Saves grouped.json: list of {cluster_name, questions}
    """
    import numpy as np

    threshold = settings.similarity_threshold

    all_embeddings_path = KNOWLEDGE_OBJECTS_PATH / textbook_name / "all_embeddings.json"
    assert all_embeddings_path.exists(), f"All embeddings path {all_embeddings_path} does not exist"
    with open(all_embeddings_path, "r", encoding="utf-8") as f:
        all_embeddings = json.load(f)

    # Flatten all knowledge objects into a flat list
    flat_items = []  # each: {question, knowledge_object, embedding, reference}
    for chunk in all_embeddings:
        ref = chunk.get("reference", 0)
        for ko in chunk.get("knowledge_objects", []):
            if "embedding" not in ko:
                continue
            flat_items.append({
                "question": ko["question"],
                "knowledge_object": ko["knowledge_object"],
                "embedding": ko["embedding"],
                "reference": ref,
            })

    if not flat_items:
        logger.warning(f"No embedded knowledge objects found for {textbook_name}")
        return

    logger.info(f"Clustering {len(flat_items)} knowledge objects with threshold={threshold}")

    embeddings = np.array([item["embedding"] for item in flat_items])

    # Normalize for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1  # avoid division by zero
    normed = embeddings / norms

    # Greedy clustering: assign each item to first cluster with similarity >= threshold
    # cluster_centroids stores the mean normed embedding of each cluster
    clusters = []          # list of lists of indices
    cluster_centroids = [] # normed centroid for each cluster

    for i in range(len(flat_items)):
        assigned = False
        if cluster_centroids:
            # Cosine similarity with all existing centroids
            centroid_matrix = np.array(cluster_centroids)
            sims = centroid_matrix @ normed[i]
            best_idx = int(np.argmax(sims))
            if sims[best_idx] >= threshold:
                clusters[best_idx].append(i)
                # Update centroid as mean of all members
                member_embeddings = normed[clusters[best_idx]]
                new_centroid = member_embeddings.mean(axis=0)
                new_centroid /= (np.linalg.norm(new_centroid) + 1e-10)
                cluster_centroids[best_idx] = new_centroid.tolist()
                assigned = True

        if not assigned:
            clusters.append([i])
            cluster_centroids.append(normed[i].tolist())

    logger.info(f"Formed {len(clusters)} clusters from {len(flat_items)} items")

    # Build grouped output
    grouped = []
    for cluster_indices in clusters:
        # Pick the knowledge_object name from the first item in the cluster
        cluster_name = flat_items[cluster_indices[0]]["knowledge_object"]
        questions = [flat_items[idx]["question"] for idx in cluster_indices]
        references = list(set(flat_items[idx]["reference"] for idx in cluster_indices))
        grouped.append({
            "cluster_name": cluster_name,
            "questions": questions,
            "references": sorted(references),
        })

    save_path = KNOWLEDGE_OBJECTS_PATH / textbook_name / "grouped.json"
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(grouped, f, indent=4, ensure_ascii=False)
    logger.info(f"Grouped knowledge saved to {save_path} ({len(grouped)} clusters)")

if __name__ == "__main__":
    # embed_textbook("Introduction to Probability by Joseph K. Blitzstein, Jessica Hwang (z-lib.org) (1).pdf")
    merge_knowledge("Introduction to Probability by Joseph K. Blitzstein, Jessica Hwang (z-lib.org) (1).pdf")