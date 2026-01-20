from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

# Import TicketResponsible for link_model
from app.models.ticket_responsible import TicketResponsible

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.board_status import BoardStatus

class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    workspace_id: int = Field()
    board_id: int = Field()
    form_id: int = Field()
    title: str = Field()
    description: Optional[str] = Field(default=None)
    requester_name: str = Field()
    requester_mail: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default=None, foreign_key="board_statuses.slug")
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)

    # Junction table relationship
    #user_links: Optional[list["TicketResponsible"]] = Relationship(
    #    back_populates="ticket")
    
    users: Optional[list["User"]] = Relationship(
        back_populates="tickets",
        link_model=TicketResponsible
    )
    
    # One-to-one relationship with BoardStatus
    board_status: Optional["BoardStatus"] = Relationship(
        back_populates="ticket",
        sa_relationship_kwargs={"foreign_keys": "[Ticket.status]"}
    )