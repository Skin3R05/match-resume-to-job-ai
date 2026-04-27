from load_data import load_job_descriptions
from matcher import compute_similarity

# Load resume
with open("../data/resumes/my_resume.txt", "r") as f:
    resume = f.read()

# Load jobs
jobs = load_job_descriptions("../data/jobs")

# Compute similarity
scores = compute_similarity(resume, jobs)

# Show top matches
top_indices = scores.argsort()[-3:][::-1]

print("\nTop matching jobs:\n")
for i in top_indices:
    print(f"Score: {scores[i]:.4f}")
    print(jobs[i][:200])
    print("\n")