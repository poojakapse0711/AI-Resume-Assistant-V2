from src.services import ask_ai


def analyze_resume(rag_chain, job_description):
    """
    Analyze the uploaded resume against a Job Description
    and generate an ATS report.
    """

    prompt = f"""
You are an experienced ATS (Applicant Tracking System).

Compare the candidate's resume with the following Job Description.

Job Description:

{job_description}

Generate the following report in Markdown format.

# ATS Score
Provide a score out of 100.

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Resume Improvement Suggestions

Be specific, practical, and recruiter-friendly.
"""

    return ask_ai(rag_chain, prompt)