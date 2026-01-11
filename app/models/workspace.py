from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.ticket import Ticket
    from app.models.ticket_responsible import TicketResponsible

class Workspace(SQLModel, table=True):
    __tablename__ = "workspaces"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    name: str = Field()
    description: Optional[str] = Field(default=None)
    logo: Optional[str] = Field(default=None)
    color: str = Field()
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)
