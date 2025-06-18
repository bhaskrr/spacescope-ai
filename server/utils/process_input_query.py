from server.llm_clients.groq_client import get_llm_client
from server.schemas.llm_schemas import LLMModerationResponse
from server.prompt_templates.templates import moderation_prompt_template


def preprocess_query(query: str) -> str:
    """
    Preprocess the user input query using rule-based methods.

    This function trims leading and trailing whitespace from the input query,
    and enforces a maximum length limit. If the query is empty after trimming,
    it is returned as-is.

    Args:
        query (str): The input query string to preprocess.

    Returns:
        str: The preprocessed query string, trimmed and length-limited.
    """
    # Remove leading and trailing whitespaces
    query = query.strip()
    # If the query is empty after trimming, return it immediately
    if query == "":
        return query

    # Define the maximum allowed length for the query
    max_length = 512
    # If the query exceeds the maximum length, truncate it
    if len(query) > max_length:
        query = query[:max_length]

    return query


def is_appropriate_with_llm(query: str) -> bool:
    """
    Check if the input query is appropriate using an LLM-based moderation chain.

    This function sends the preprocessed query to an LLM moderation chain,
    which uses a prompt template and expects a structured JSON response
    indicating whether the content is appropriate.

    Args:
        query (str): The input text to check for appropriateness.

    Returns:
        bool: True if the query is appropriate, False otherwise.
    """
    # Get the LLM client instance
    client = get_llm_client()
    # Configure the LLM to expect a structured output matching LLMModerationResponse
    llm = client.with_structured_output(LLMModerationResponse, method="json_mode")

    # Create the moderation chain by combining the prompt template and the LLM
    chain = moderation_prompt_template | llm

    # Invoke the chain with the user input and get the response
    response = chain.invoke({"user_input": query})

    # Return True if the response indicates appropriateness, otherwise False
    if response.is_appropriate is True:
        return True
    return False