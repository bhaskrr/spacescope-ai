from pydantic import BaseModel


class LLMModerationResponse(BaseModel):
    is_appropriate: bool
    reason: str | None = None


class DirectLLMResponse(BaseModel):
    answer: str


class RAGLLMResponse(BaseModel):
    answer: str