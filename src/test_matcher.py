from load_data import load_job_descriptions
from matcher import compute_similarity
from skill_matcher import get_missing_skills

# Load resume
with open("../data/resumes/my_resume.txt", "r") as f:
    resume = f.read()

# Load jobs
jobs = load_job_descriptions("../data/jobs")

# Compute similarity
scores = compute_similarity(resume, jobs)

# Top match
top_index = scores.argmax()
top_job = jobs[top_index]

print(f"\nBest match score: {scores[top_index]:.4f}\n")

# Skill comparison
missing, resume_skills, job_skills = get_missing_skills(resume, top_job)

print("Your skills:", resume_skills)
print("\nJob requires:", job_skills)
print("\nMissing skills:", missing)