import os
from typing import LiteralString
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())


class AppSettings:
    CHROMA_HOST: LiteralString = os.environ.get("CHROMA_HOST")
    CHROMA_PORT: int = os.environ.get("CHROMA_PORT")
    CHROMA_TOKEN: LiteralString = os.environ.get("CHROMA_TOKEN")
