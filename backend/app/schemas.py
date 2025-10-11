from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    country: Optional[str] = "ghana"
    industry: Optional[str] = "general"

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    country: str
    industry: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ChatRequest(BaseModel):
    message: str
    country: Optional[str] = "ghana"
    industry: Optional[str] = "general"
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    confidence: float
    conversation_id: Optional[int] = None
    ai_error: Optional[str] = None
