from pydantic import BaseModel
from typing import List, Optional


class LLMModerationResponse(BaseModel):
    is_appropriate: bool
    reason: str | None = None


