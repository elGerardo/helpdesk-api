from app.models.user import User
from sqlmodel import select
from app.utils.query import first_or_fail

class UserService:

    async def find(user_name: str) -> User:
        query = select(User).where(User.user_name == user_name)
        result = await first_or_fail(
            query = query
        )
        return result