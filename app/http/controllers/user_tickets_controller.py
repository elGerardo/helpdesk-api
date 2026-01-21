from starlette.responses import JSONResponse
from starlette.requests import Request 
from app.http.services.user_ticket_service import UserTicketService
from app.http.dtos.user_tickets.filter_user_tickets_dto import FilterUserTicketDto
from app.utils.http_status import ok

class UserTicketsController:
    
    async def index(request: Request) -> JSONResponse:
        query_params = FilterUserTicketDto(**request.query_params)
        result = await UserTicketService.get_all(request.state.user, query_params)
        return ok(result)