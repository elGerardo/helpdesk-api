from app.models.ticket_responsible import TicketResponsible
from config.database import get_session

class TicketResponsibleService:
    @staticmethod
    async def store(user_id: int, ticket_id: int, tenant_id: int, session=None) -> TicketResponsible:
        if session is None:
            session = next(get_session())

        ticket_responsible = TicketResponsible(
            user_id=user_id,
            ticket_id=ticket_id,
            tenant_id=tenant_id
        )
        session.add(ticket_responsible)
        session.flush()

        return ticket_responsible
