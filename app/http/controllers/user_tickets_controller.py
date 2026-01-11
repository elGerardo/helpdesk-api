from starlette.responses import JSONResponse
from starlette.requests import Request 
from app.http.services.user_ticket_service import UserTicketService
from app.utils.http_status import ok

class UserTicketsController:
    
    async def index(request: Request) -> JSONResponse:
        result = await UserTicketService.get_all(request.state.user)
        return ok(result)