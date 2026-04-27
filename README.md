# AI Resume–Job Matching System (RAG + Semantic Search)

## Overview

This project is a Retrieval-Augmented Generation (RAG) system that matches resumes with job descriptions using semantic search and machine learning techniques. It helps users understand how well their resume fits a job role, identifies missing skills, and provides AI-generated explanations.

---

## Problem Statement

Job seekers often struggle to evaluate:
- How well their resume matches a job description
- Which skills they are missing for a role
- Which job roles best fit their profile

This system addresses these challenges using embeddings, vector search, and language models.

---

## Features

- Upload resume in text format
- Semantic search over job descriptions
- Resume-to-job matching using embeddings
- Match scoring using vector similarity
- Identification of missing skills
- AI-generated explanation of job fit
- Streamlit-based user interface

---

## Tech Stack

- Python
- Sentence Transformers (Hugging Face)
- FAISS (Vector Database)
- Streamlit (Frontend)
- Transformers (Language Model for explanations)

---

## System Architecture

The system follows a Retrieval-Augmented Generation pipeline:

1. Resume and job descriptions are converted into embeddings
2. FAISS is used to store and retrieve similar job descriptions
3. Top matching jobs are retrieved based on similarity score
4. A language model generates explanations and insights
5. Missing skills are extracted by comparing resume and job requirements

---

## Workflow

User Resume → Embedding Model → Vector Database (FAISS)
Job Descriptions → Embedding Model → Stored in FAISS
Query → Semantic Search → Top Matches → LLM Explanation → Output

---

## Example Output

Input:
- Resume: Python, SQL, Machine Learning, Pandas
- Job: Data Scientist requiring Python, PyTorch, TensorFlow

Output:
- Match Score: 0.53
- Missing Skills: PyTorch, TensorFlow
- Explanation: The resume matches core data science skills but lacks deep learning frameworks required for this role.

---

## Project Structure

rag-resume-matcher/
│
├── src/
│ ├── app.py
│ ├── load_data.py
│ ├── vector_store.py
│ ├── matcher.py
│ ├── llm.py
│
├── data/
│ ├── jobs/
│ ├── resumes/
│
├── requirements.txt
├── README.md


---

## Key Learnings

- Building a RAG pipeline from scratch
- Working with embeddings for semantic search
- Using FAISS for efficient similarity search
- Integrating language models for explanation generation
- Designing an end-to-end ML application with UI

---

## Limitations

- Uses simple text-based resume input
- Basic skill extraction logic
- Lightweight language model for explanation generation
- No database or persistent storage layer

---

## Future Improvements

- Support for PDF resume parsing
- Improved skill extraction using NLP models
- Integration with real job APIs (LinkedIn, Indeed)
- Deployment on cloud platforms
- Better instruction-tuned language model
- Authentication and user profiles

---

## How to Run

Install dependencies: pip install -r requirements.txt

Run Streamlit app: streamlit run src/app.py


---

## Author

Machine Learning project focused on RAG systems, semantic search, and resume-job matching.

