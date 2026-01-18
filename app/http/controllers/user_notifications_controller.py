from starlette.responses import JSONResponse
from starlette.requests import Request 
from app.http.services.user_notification_service import UserNotificationService
from app.utils.http_status import ok

class UserNotificationsController:
    
    async def index(request: Request) -> JSONResponse:
        result = await UserNotificationService.get_all(request.state.user)
        return ok(result)
