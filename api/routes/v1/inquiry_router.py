from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.schemas.inquiry_schema import MessageCreate, MessageResponse
from api.services.inquiry_service import MessageService
from api.repositories.inquiry_repository import MessageRepository
from api.utils.database import get_db

router = APIRouter(
    tags=["Inquiries"],
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Not found"},
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
    }
)

@router.post("/", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def create_inquiry(
    message: MessageCreate, 
    db: AsyncSession = Depends(get_db)
):
    message_repo = MessageRepository(db)
    message_service = MessageService(message_repo)
    return await message_service.create_message(message)

@router.get("/{message_id}", response_model=MessageResponse)
async def get_inquiry(
    message_id: int,
    db: AsyncSession = Depends(get_db)  # Note AsyncSession
):
    message_repo = MessageRepository(db)
    message_service = MessageService(message_repo)
    db_message = await message_service.get_message(message_id)  # Add await
    if not db_message:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message