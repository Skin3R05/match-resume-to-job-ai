import streamlit as st

from load_data import load_job_descriptions
from vector_store import create_embeddings, create_faiss_index, search, model
from llm import generate_answer

st.set_page_config(page_title="Resume Matcher AI", layout="centered")

st.title("🧠 Resume–Job Matching AI (RAG System)")


# ----------------------------
# CACHE JOB DATA (IMPORTANT)
# ----------------------------
@st.cache_data
def get_jobs():
    return load_job_descriptions()


# ----------------------------
# CACHE VECTOR STORE (CRITICAL PERFORMANCE FIX)
# ----------------------------
@st.cache_resource
def build_index():
    jobs = get_jobs()
    texts, embeddings = create_embeddings(jobs)
    index = create_faiss_index(embeddings)
    return jobs, texts, index


jobs, texts, index = build_index()


# ----------------------------
# UI INPUTS
# ----------------------------
query = st.text_input(
    "Enter job requirements",
    placeholder="e.g. Data Scientist with Python, SQL, Machine Learning"
)

uploaded_file = st.file_uploader("Upload Resume (TXT)", type=["txt"])

resume_text = ""
if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")


# ----------------------------
# SEARCH BUTTON
# ----------------------------
if st.button("Search"):

    if not query:
        st.warning("Please enter job requirements")
        st.stop()

    # Step 1: Retrieve relevant job chunks
    results = search(query, model, index, texts)

    # Step 2: Generate AI answer
    answer = generate_answer(query, results)

    # ----------------------------
    # OUTPUT
    # ----------------------------
    st.subheader("📊 AI Analysis")

    st.markdown("### 🧠 Answer")
    st.write(answer)

    st.markdown("### 🔍 Top Matching Job Snippets")
    for r in results:
        st.info(r[:300])