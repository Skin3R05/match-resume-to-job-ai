from skill_extractor import extract_skills


def get_missing_skills(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    missing = job_skills - resume_skills

    return missing, resume_skills, job_skills
