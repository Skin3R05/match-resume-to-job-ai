from load_data import load_job_descriptions, chunk_documents
from vector_store import create_embeddings, create_faiss_index, search, model

# Load + chunk
jobs = load_job_descriptions("../data/jobs")
chunks = chunk_documents(jobs)

# Convert to embeddings
texts, embeddings = create_embeddings(chunks)

# Create vector DB
index = create_faiss_index(embeddings)

# Test query
query = "What skills are required for a data scientist?"

results = search(query, model, index, texts)

print("\nTop results:\n")
for r in results:
    print("-", r[:200], "\n")