import re

# simple skill list (we can expand later)
SKILLS = [
    "python", "sql", "machine learning", "deep learning",
    "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy", "databricks", "aws", "docker"
]


def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.add(skill)

    return found_skills
