from starlette.requests import Request 
from app.http.dtos.auth.login_dto import LoginDTO
from app.utils.http_status import created, ok
from starlette.responses import JSONResponse
from config.database import get_session
from config.app import HASH
from app.models.user import User
from sqlmodel import select, or_
import jwt
from datetime import datetime, timezone, timedelta
from config.app import JWT_SECRET, JWT_HASH, ACCESS_TOKEN_EXPIRE_MINUTES

class AuthController:

    async def login(request: Request) -> JSONResponse:
        payload = request.state.body
            
        dto = LoginDTO.model_validate(payload)
        session = next(get_session())
        res = select(User).where(
            or_(
                User.email == dto.identifier,
                User.user_name == dto.identifier
            )
        )
        user: User = session.exec(res).first()

        if not user:
            return JSONResponse({
                "error": "Invalid credentials"
            }, status_code=401)

        hash_verified = HASH.verify(dto.password, user.password)
        if not hash_verified:
            return JSONResponse({
                "error": "Invalid credentials"
            }, status_code=401)

        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"sub": str(user.id)}
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_HASH)

        return created(user.model_dump() | {"access_token": encoded_jwt, "token_type": "bearer"})

    async def me(request: Request) -> JSONResponse:
        auth_header = request.headers.get("Authorization")
        auth_header = auth_header.split(" ")[1]
        payload = jwt.decode(auth_header, JWT_SECRET, algorithms=[JWT_HASH])
        userId = payload.get("sub")

        session = next(get_session())
        res = select(User).where(User.id == userId)
        user: User = session.exec(res).first()
        
        return ok(user) 