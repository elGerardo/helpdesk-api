from app.models.user import User
from config.database import get_session
from config.app import HASH
from sqlmodel import select

class UserService:

    async def find_or_store(user_name: str) -> User:
        session = next(get_session())
        res = select(User).where(User.user_name == user_name)
        user: User = session.exec(res).first()

        if not user:
            user = User(**{
                'name': 'name5', 
                'last_name': 'last_name5', 
                'user_name': 'user_name5', 
                'email': 'user5@mail.com', 
                'password': HASH.hash('12345')
            }).create()

        return user