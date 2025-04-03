from fastapi import APIRouter
from .inquiry_router import router as inquiry_router

router = APIRouter()

router.include_router(inquiry_router, prefix="/api/v1/inquiries", tags=["Inquiries"])