from app.models.user import User
from app.models.ticket import Ticket
from app.models.ticket_responsible import TicketResponsible
from sqlmodel import select
from app.utils.query import get


class UserTicketService:

    async def get_all(logged_user: User, session=None) -> list[Ticket]:
        query = (
            select(Ticket)
            .join(TicketResponsible, Ticket.id == TicketResponsible.ticket_id)
            .where(TicketResponsible.user_id == logged_user.id)
            .where(TicketResponsible.tenant_id == logged_user.tenant_id)
        )
        
        result = await get(None, query)

        return result
