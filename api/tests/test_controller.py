from api.utils.app_response import AppResponse
from api.tests.test_service import TestService
# from api.services

class TestController:
    """
    Controller for handling the test route logic.
    """

    def __init__(self):
        self.test_service = TestService()

    async def get_hello_world(self):
        """
        Logic for the test route.

        Returns:
            JSONResponse: A standardized response with "Hello World".
        """
        # Call the service to get the message
        message = await self.test_service.get_hello_world()
        return AppResponse.send_success(
            data={"message": message},
            message="Test route executed successfully"
        )
