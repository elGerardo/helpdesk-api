from app.http.dtos.user_notifications.filter_user_notifications_dto import FilterUserNotificationsDto
from app.models.user import User
from app.models.notification import Notification
from sqlmodel import select
from app.utils.query import get

class UserNotificationService:

    async def get_all(logged_user: User, filters: FilterUserNotificationsDto, session=None) -> list[Notification]:
        query = (
            select(Notification)
            .where(Notification.deliveried_to == logged_user.id)
        )
        
        result = await get(
            query=query, 
            fields_to_serialize=True,
            pagination={'page': filters.page, 'limit': filters.limit},
        )

        return result
