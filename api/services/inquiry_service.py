from api.repositories.inquiry_repository import MessageRepository
from api.schemas.inquiry_schema import MessageCreate, MessageResponse

class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository
    
    async def create_message(self, message: MessageCreate) -> MessageResponse:
        return await self.message_repository.create_message(message)  # Add await
    
    async def get_message(self, message_id: int) -> MessageResponse:
        return await self.message_repository.get_message(message_id)  # Add await
    
    async def get_messages(self, skip: int = 0, limit: int = 100) -> list[MessageResponse]:
        return await self.message_repository.get_messages(skip, limit)  # Add await