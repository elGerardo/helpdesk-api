from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import json


class JSONValidationMiddleware(BaseHTTPMiddleware):
    """Middleware to validate JSON payloads and attach parsed body to request."""
    
    async def dispatch(self, request: Request, call_next):
        request.state.body = {}
        
        if request.method in ['POST', 'PUT', 'PATCH']:
            content_type = request.headers.get('content-type', '')
            
            if 'application/json' in content_type:
                request.state.body = await request.json()

        response = await call_next(request)
        return response
