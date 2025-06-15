import chromadb
from chromadb.config import Settings
from server.config.settings import AppSettings


def get_client():
    """Creates a Chroma client with the service URL and API token and returns it."""
    client = chromadb.HttpClient(
        host=AppSettings.CHROMA_HOST,
        port=AppSettings.CHROMA_PORT,
        ssl=True,
        settings=Settings(
            chroma_client_auth_provider="chromadb.auth.token_authn.TokenAuthClientProvider",
            chroma_client_auth_credentials=AppSettings.CHROMA_TOKEN,
            anonymized_telemetry=False,
        ),
    )
    return client
