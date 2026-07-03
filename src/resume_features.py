def generate_summary(rag_chain):

    prompt = """
    Give a professional summary of this resume.

    Include:

    • Candidate Profile

    • Years of Experience

    • Technical Skills

    • Domain Knowledge

    Keep it under 200 words.
    """

    response = rag_chain.invoke(
        {
            "input": prompt
        }
    )

    return response["answer"]


def extract_skills(rag_chain):

    prompt = """
    Extract all technical skills from this resume.

    Group them into:

    • Programming Languages

    • Databases

    • Frameworks

    • Cloud

    • Tools

    • Soft Skills
    """

    response = rag_chain.invoke(
        {
            "input": prompt
        }
    )

    return response["answer"]


def interview_questions(rag_chain):

    prompt = """
    Based on this resume,

    generate 10 interview questions.

    Mix:

    • Technical

    • Project

    • Behavioural
    """

    response = rag_chain.invoke(
        {
            "input": prompt
        }
    )

    return response["answer"]


def improvement_suggestions(rag_chain):

    prompt = """
    Review this resume.

    Suggest improvements.

    Include

    • ATS

    • Formatting

    • Missing Skills

    • Resume Quality

    Give practical suggestions.
    """

    response = rag_chain.invoke(
        {
            "input": prompt
        }
    )

    return response["answer"]