from src.services import ask_ai


def generate_cover_letter(rag_chain, job_description):
    """
    Generate a professional cover letter based on the
    uploaded resume and job description.
    """

    prompt = f"""
You are an expert career coach and HR recruiter.

The candidate's resume is already available as context.

Below is the Job Description.

--------------------------

{job_description}

--------------------------

Write a professional cover letter.

Requirements:

- Address the Hiring Manager
- Mention why the candidate is interested
- Highlight the most relevant experience
- Explain how the candidate fits the role
- Keep it professional
- Keep it under 400 words
- End politely

Return only the cover letter.
"""

    return ask_ai(rag_chain, prompt)