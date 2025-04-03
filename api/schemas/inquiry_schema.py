from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class MessageBase(BaseModel):
    name: str
    email: EmailStr
    message: str

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    created_at: datetime
    is_responded: bool
    
    class Config:
        from_attributes = True