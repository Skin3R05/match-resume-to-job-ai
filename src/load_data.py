import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOBS_PATH = os.path.join(BASE_DIR, "data", "jobs")


def load_job_descriptions(folder_path=JOBS_PATH):
    documents = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Jobs folder not found at: {folder_path}")

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                documents.append(file.read())

    return documents