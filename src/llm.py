from transformers import pipeline

# Load model (this was missing or removed)
generator = pipeline("text-generation", model="gpt2")


def generate_answer(query, retrieved_docs):
    context = "\n".join(retrieved_docs)

    prompt = f"""
You are a helpful assistant.

Use ONLY the information from the context below to answer the question.
Be concise and list key skills clearly.

Context:
{context}

Question:
{query}

Answer (bullet points):
"""

    result = generator(
        prompt,
        max_new_tokens=150,
        do_sample=False
    )

    return result[0]["generated_text"]