from fastapi import APIRouter
from api.tests.test_controller import TestController

router = APIRouter()


test_controller = TestController()

@router.get("/")
async def test_route():
    """
    A simple test route returning Hello World.
    """
    return await test_controller.get_hello_world()


@router.get("/test")
async def test_route():
    """
    A simple test route returning Hello World.
    """
    return await test_controller.get_hello_world()