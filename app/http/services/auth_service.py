from app.http.dtos.auth.login_dto import LoginDTO
from config.database import get_session
from config.app import HASH
from app.models.user import User
from app.models.notification import Notification
from sqlmodel import select, or_
import jwt
from datetime import datetime, timedelta
from config.app import JWT_SECRET, JWT_HASH, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_LIMIT_SECONDS
from app.utils.query import get, first_or_fail

class AuthService:
    async def login(dto: LoginDTO) -> dict:            
        session = next(get_session())
        res = select(User).where(
            or_(
                User.email == dto.identifier,
                User.user_name == dto.identifier
            )
        )
        user: User = session.exec(res).first()

        if not user:
            return {
                "error": "Invalid credentials"
            }

        hash_verified = HASH.verify(dto.password, user.password)
        if not hash_verified:
            return {
                "error": "Invalid credentials"
            }
        
        time = (ACCESS_TOKEN_EXPIRE_MINUTES + (REFRESH_TOKEN_LIMIT_SECONDS / 60))
        expires_delta = timedelta(minutes=time)

        to_encode = {"sub": str(user.id)}
        expire = datetime.now() + expires_delta

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_HASH)

        return { 
            "access_token": encoded_jwt, 
            "token_type": "bearer", 
        }

    async def logout() -> dict:
        
        return {
            "message": "Successfully logged out"
        }

    async def me(token: str) -> dict:
        auth_header = token
        auth_header = auth_header.split(" ")[1]
        payload = jwt.decode(auth_header, JWT_SECRET, algorithms=[JWT_HASH])
        userId = payload.get("sub")

        session = next(get_session())

        user_query = select(User).where(User.id == userId)
        user: User = await first_or_fail(session=session, query=user_query, error_message="User not found")

        notifications_query = select(Notification).where(Notification.deliveried_to == userId)
        notifications = await get(session=session, query=notifications_query)

        return {
            "user": user,
            "notifications": notifications
        }

    async def refresh(token: str) -> dict:
        try:
            auth_header = token
            auth_header = auth_header.split(" ")[1]
            payload = jwt.decode(auth_header, JWT_SECRET, algorithms=[JWT_HASH])
            userId = payload.get("sub")

            if not userId:
                return {
                    "error": "Invalid token"
                }

            session = next(get_session())
            user_query = select(User).where(User.id == userId)
            user: User = session.exec(user_query).first()

            if not user:
                return {
                    "error": "User not found"
                }

            # Generate new token
            expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES + (REFRESH_TOKEN_LIMIT_SECONDS / 60))
            to_encode = {"sub": str(user.id)}
            expire = datetime.now() + expires_delta
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_HASH)

            return {
                "access_token": encoded_jwt,
                "token_type": "bearer"
            }
        except jwt.ExpiredSignatureError:
            return {
                "error": "Token has expired"
            }
        except jwt.InvalidTokenError:
            return {
                "error": "Invalid token"
            }

    async def token_info(token: str) -> dict:
        try:
            auth_header = token
            auth_header = auth_header.split(" ")[1]
            payload = jwt.decode(auth_header, JWT_SECRET, algorithms=[JWT_HASH])
            
            exp_timestamp = payload.get("exp")
            user_id = payload.get("sub")
            
            if not exp_timestamp:
                return {
                    "error": "Token missing expiration"
                }
            
            # Convert timestamp to datetime
            expiration_time = datetime.fromtimestamp(exp_timestamp)
            current_time = datetime.now()
            
            # Calculate remaining time
            time_remaining = expiration_time - current_time
            remaining_seconds = int(time_remaining.total_seconds())
            
            return {
                "user_id": user_id,
                "expires_at": expiration_time.isoformat(),
                "current_time": current_time.isoformat(),
                "remaining_seconds": remaining_seconds,
                "remaining_minutes": round(remaining_seconds / 60, 2),
                "is_expired": remaining_seconds <= 0
            }
        except jwt.ExpiredSignatureError:
            return {
                "error": "Token has expired",
                "is_expired": True
            }
        except jwt.InvalidTokenError:
            return {
                "error": "Invalid token"
            }