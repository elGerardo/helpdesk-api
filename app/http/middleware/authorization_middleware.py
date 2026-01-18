from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request
import jwt
from sqlmodel import select
from datetime import datetime, timezone

from app.http.middleware.kernel import kernel
from app.models.user import User
from config.database import get_session
from config.app import JWT_SECRET, JWT_HASH, REFRESH_TOKEN_LIMIT_SECONDS


class AuthorizationMiddleware(BaseHTTPMiddleware):
    """Middleware to validate Authorization header for protected endpoints."""
    
    async def dispatch(self, request: Request, call_next):
        #if request.url.path in kernel['authorization_middleware_exceptions']:
        #    response = await call_next(request)
        #    return response
        
        authorization = request.headers.get('authorization')
        
        if not authorization:
            return JSONResponse({
                "error": "Unauthorized"
            }, status_code=401)
        
        if not authorization.startswith('Bearer '):
            return JSONResponse({
                "error": "Unauthorized"
            }, status_code=401)
        
        token = authorization.replace('Bearer ', '')
        request.state.token = token
        
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_HASH])
            exp_timestamp = payload.get("exp")
            user_id = payload.get("sub")

            
            expiration_time = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
            current_time = datetime.now(timezone.utc)
            time_remaining = expiration_time - current_time
            remaining_seconds = int(time_remaining.total_seconds())
            
            if remaining_seconds <= REFRESH_TOKEN_LIMIT_SECONDS:
                return JSONResponse({
                    "error": "Unauthorized"
                }, status_code=401)
        
            session = next(get_session())
            res = select(User).where(User.id == user_id)
            user: User = session.exec(res).first()
            
            if not user:
                return JSONResponse({
                    "error": "Unauthorized"
                }, status_code=401)
            
            # Add user to request state
            request.state.user = user
            
        except jwt.ExpiredSignatureError:
            return JSONResponse({
                "error": "Unauthorized"
            }, status_code=401)
        except jwt.InvalidTokenError:
            return JSONResponse({
                "error": "Unauthorized"
            }, status_code=401)
        except Exception as e:
            return JSONResponse({
                "error": "Unauthorized"
            }, status_code=401)
        
        response = await call_next(request)
        return response
