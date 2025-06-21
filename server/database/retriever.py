from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from server.database.client import get_client

default_ef = DefaultEmbeddingFunction()


def retrieve_relevant_documents(query: str) -> dict:
    """Retrieves relevant documents from the vector database
    
    Args:
        query (str): The input query
    
    Returns:
        relevant_docs (dict): The retrieved docs
    
    """
    # Initialize the vector database client
    client = get_client()

    # Get the collection
    collection = client.get_collection(name="space_docs", embedding_function=default_ef)

    # Query the collection
    relevant_docs = collection.query(query_texts=query, n_results=7)

    # Return the retrieved documents
    return relevant_docs
