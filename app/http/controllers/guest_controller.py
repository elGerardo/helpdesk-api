from starlette.responses import JSONResponse
from starlette.requests import Request
from app.http.services.guest_service import GuestService
from app.utils.http_status import created

class GuestController:
        
    async def store(request: Request) -> JSONResponse:
        result = await GuestService.store()
        return created(result)