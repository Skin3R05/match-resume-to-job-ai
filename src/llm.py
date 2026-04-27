from transformers import pipeline

# Better instruction-tuned model (much improved)
generator = pipeline(
    "text-generation",
    model="tiiuae/falcon-rw-1b"
)


def generate_answer(query, retrieved_docs):
    context = "\n".join(retrieved_docs)

    prompt = f"""
You are a professional AI assistant for resume-job matching.

Use ONLY the context below.

Context:
{context}

Question:
{query}

Answer in clear bullet points:
"""

    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.3
    )

    return result[0]["generated_text"]