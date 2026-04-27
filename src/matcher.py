from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_similarity(resume_text, job_texts):
    resume_embedding = model.encode([resume_text])
    job_embeddings = model.encode(job_texts)

    similarities = np.dot(job_embeddings, resume_embedding.T).flatten()

    return similarities