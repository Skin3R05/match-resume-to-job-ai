import streamlit as st
from load_data import load_job_descriptions, chunk_documents
from vector_store import create_embeddings, create_faiss_index, search, model
from llm import generate_answer

st.title("🧠 Resume–Job Matching AI (RAG System)")

query = st.text_input("Ask something about job requirements:")

if st.button("Search"):
    jobs = load_job_descriptions("../data/jobs")
    chunks = chunk_documents(jobs)

    texts, embeddings = create_embeddings(chunks)
    index = create_faiss_index(embeddings)

    results = search(query, model, index, texts)

    answer = generate_answer(query, results)

    st.subheader("AI Answer")
    st.write(answer)

uploaded_file = st.file_uploader("Upload Resume (txt)", type=["txt"])

resume_text = ""
if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")