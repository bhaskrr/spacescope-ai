from server.utils.process_input_query import preprocess_query, is_appropriate_with_llm

def process_and_check_input_appropriateness(query: str) -> bool:
    """
    Preprocesses a user input query and checks its appropriateness using an LLM-based moderation function.

    This function performs two main steps:
    1. Preprocesses the input query by trimming whitespace and enforcing length limits or other normalization.
    2. Uses an LLM moderation utility to determine if the preprocessed query is appropriate for a general audience.

    Args:
        query (str): The raw user input to be checked.

    Returns:
        bool: True if the input is appropriate, False otherwise.
    """
    # Step 1: Preprocess the input (e.g., trim, normalize, enforce length limits)
    preprocessed_query = preprocess_query(query)
    # Step 2: Use the LLM moderation function to check appropriateness
    is_appropriate = is_appropriate_with_llm(preprocessed_query)
    return is_appropriate