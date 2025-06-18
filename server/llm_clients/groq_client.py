from langchain_groq import ChatGroq


def get_llm_client(model_name="llama-3.1-8b-instant"):
    """Initializes an llm client with the specified model name.

    Args:
        model_name (str): Name of the model. Defaults to "llama-3.1-8b-instant"
    Returns:
        llm_client (ChatGroq): The llm client
    """
    llm_client = ChatGroq(model=model_name, temperature=0.5)
    return llm_client
