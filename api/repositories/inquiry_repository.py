from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy.future import select
from api.models.inquiry_model import Message
from api.schemas.inquiry_schema import MessageCreate

class MessageRepository:
    def __init__(self, db: AsyncSession):  # Changed to AsyncSession
        self.db = db
    
    async def create_message(self, message: MessageCreate):
        try:
            db_message = Message(**message.model_dump())
            self.db.add(db_message)
            await self.db.commit()
            await self.db.refresh(db_message)
            return db_message  # You can modify to return custom status message if needed
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating message: {str(e)}")
    
    async def get_message(self, message_id: int):
        result = await self.db.execute(
            select(Message).where(Message.id == message_id)  # Using select with where
        )
        return result.scalars().first()  # Using scalars() for single result
    
    async def get_messages(self, skip: int = 0, limit: int = 100):
        result = await self.db.execute(
            select(Message).offset(skip).limit(limit)  # Modern SQLAlchemy query
        )
        return result.scalars().all()  # Using scalars() for multiple results