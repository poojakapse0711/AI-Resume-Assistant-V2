def ask_ai(rag_chain, prompt):
    """
    Sends a prompt to the RAG chain and returns the generated answer.
    """

    response = rag_chain.invoke(
        {
            "input": prompt
        }
    )

    return response["answer"]