from src.services import ask_ai


def generate_summary(rag_chain):
    """
    Generate a professional summary of the uploaded resume.
    """

    prompt = """
You are an expert HR recruiter.

Generate a professional summary of this resume.

Include:

• Candidate Profile

• Years of Experience

• Technical Skills

• Domain Knowledge

Keep the summary under 200 words.
"""

    return ask_ai(rag_chain, prompt)


def extract_skills(rag_chain):
    """
    Extract technical and soft skills from the resume.
    """

    prompt = """
Extract all skills from this resume.

Group them into the following categories.

Programming Languages

Databases

Frameworks

Cloud Technologies

Tools

Soft Skills

Return the result in Markdown format.
"""

    return ask_ai(rag_chain, prompt)


def interview_questions(rag_chain):
    """
    Generate interview questions based on the resume.
    """

    prompt = """
Generate 10 interview questions based on this resume.

Include:

• Technical Questions

• Project Based Questions

• Behavioural Questions

Return the output in Markdown.
"""

    return ask_ai(rag_chain, prompt)


def improvement_suggestions(rag_chain):
    """
    Suggest improvements for the resume.
    """

    prompt = """
Review this resume.

Suggest improvements.

Focus on:

• ATS Optimization

• Resume Formatting

• Missing Skills

• Quantifying Achievements

• Professional Summary

Return the result in Markdown.
"""

    return ask_ai(rag_chain, prompt)