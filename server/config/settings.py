import os
from typing import LiteralString, List
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())


class AppSettings:
    CHROMA_HOST: LiteralString = os.environ.get("CHROMA_HOST")
    CHROMA_PORT: int = os.environ.get("CHROMA_PORT")
    CHROMA_TOKEN: LiteralString = os.environ.get("CHROMA_TOKEN")
    CORS_ORIGINS: List[str] = os.environ.get("CORS_ORIGINS")
    CORS_METHODS: List[str] = os.environ.get("CORS_METHODS")
    CORS_HEADERS: List[str] = os.environ.get("CORS_HEADERS")
