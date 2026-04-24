import os
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_job_descriptions(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                text = file.read()
                documents.append(text)

    return documents


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.create_documents(documents)
    return chunks


if __name__ == "__main__":
    jobs = load_job_descriptions("../data/jobs")
    chunks = chunk_documents(jobs)

    print(f"Total chunks created: {len(chunks)}")
    print("\nSample chunk:\n")
    print(chunks[0].page_content)