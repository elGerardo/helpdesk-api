from starlette.responses import JSONResponse
from starlette.requests import Request 
from app.http.services.user_notification_service import UserNotificationService
from app.http.dtos.user_notifications.filter_user_notifications_dto import FilterUserNotificationsDto
from app.utils.http_status import ok

class UserNotificationsController:
    
    async def index(request: Request) -> JSONResponse:
        query_params = FilterUserNotificationsDto(**request.query_params)
        result = await UserNotificationService.get_all(request.state.user, query_params)
        return ok(result)
