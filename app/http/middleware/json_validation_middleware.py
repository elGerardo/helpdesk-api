from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
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

        # Continue to the endpoint
        response = await call_next(request)
        return response
