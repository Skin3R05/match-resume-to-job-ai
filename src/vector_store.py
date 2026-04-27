from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model (this converts text → vectors)
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts)
    return texts, embeddings


def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index


def search(query, model, index, texts, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)

    results = [texts[i] for i in indices[0]]
    return results