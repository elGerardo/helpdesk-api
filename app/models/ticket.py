from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

# Import TicketResponsible for link_model
from app.models.ticket_responsible import TicketResponsible

if TYPE_CHECKING:
    from app.models.user import User

class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    workspace_id: int = Field()
    board_id: int = Field()
    form_id: int = Field()
    requester_name: str = Field()
    requester_mail: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)

    # Junction table relationship
    #user_links: Optional[list["TicketResponsible"]] = Relationship(
    #    back_populates="ticket")
    
    # Direct many-to-many relationship to users
    users: Optional[list["User"]] = Relationship(
        back_populates="tickets",
        link_model=TicketResponsible
    )