from load_data import load_job_descriptions, chunk_documents
from vector_store import create_embeddings, create_faiss_index, search, model
from llm import generate_answer

jobs = load_job_descriptions("../data/jobs")
chunks = chunk_documents(jobs)

texts, embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

query = "What skills are required for a data scientist?"

retrieved_docs = search(query, model, index, texts)

answer = generate_answer(query, retrieved_docs)

print("\nFinal Answer:\n")
print(answer)