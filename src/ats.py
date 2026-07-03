def analyze_resume(rag_chain, job_description):

    prompt = f"""
You are an experienced ATS (Applicant Tracking System).

Compare the candidate's resume with the following Job Description.

Job Description:

{job_description}

Generate the following report in markdown format.

# ATS Score
Give a score out of 100.

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Resume Improvement Suggestions

Be specific and practical.
"""

    response = rag_chain.invoke(
        {
            "input": prompt
        }
    )

    return response["answer"]