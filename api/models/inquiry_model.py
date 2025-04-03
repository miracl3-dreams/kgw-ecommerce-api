from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from api.utils.database import Base
from ..models import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    message = Column(String(1000), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_responded = Column(Boolean, default=False)