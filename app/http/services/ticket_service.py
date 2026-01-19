from app.http.dtos.tickets.store_ticket_dto import StoreTicketDTO
from app.models.ticket import Ticket
from config.database import get_session

class TicketService:
    @staticmethod
    async def store(dto: StoreTicketDTO, session=None) -> Ticket:
        if session is None:
            session = next(get_session())

        ticket = Ticket(
            tenant_id=dto.tenant_id,
            workspace_id=dto.workspace_id,
            board_id=dto.board_id,
            form_id=dto.form_id,
            requester_name=dto.requester_name,
            requester_mail=dto.requester_mail,
            status=dto.status
        )
        session.add(ticket)
        session.flush()

        return ticket
