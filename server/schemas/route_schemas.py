from pydantic import BaseModel
from enum import Enum


class ModeEnum(Enum):
    normal = "normal"
    rag = "rag"


class InputQuery(BaseModel):
    query: str
    mode: ModeEnum
