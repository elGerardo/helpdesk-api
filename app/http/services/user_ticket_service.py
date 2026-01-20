from app.models.user import User
from app.models.ticket import Ticket
from app.models.ticket_responsible import TicketResponsible
from app.models.board_status import BoardStatus
from sqlmodel import select
from sqlalchemy.orm import joinedload
from app.utils.query import get
from app.utils.serializer import Serializer

class UserTicketService:

    async def get_all(logged_user: User, session=None) -> list[Ticket]:
        query = (
            select(Ticket)
            .join(TicketResponsible, Ticket.id == TicketResponsible.ticket_id)
            .where(TicketResponsible.user_id == logged_user.id)
            .where(TicketResponsible.tenant_id == logged_user.tenant_id)
            .options(joinedload(Ticket.board_status))
        )
        
        result = await get(
            query=query, 
            fields_to_serialize=['board_status']
        )
#        result = Serializer.serialize(result, fields_to_serialize=['board_status'])

        return result
