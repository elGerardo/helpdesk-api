from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.models.ticket import Ticket

class BoardStatus(SQLModel, table=True):
    __tablename__ = "board_statuses"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    board_id: int = Field()
    label: str = Field()
    slug: str = Field(unique=True)
    type: str = Field()  # DEFAULT | CUSTOM
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)
    
    # One-to-one relationship with Ticket
    ticket: Optional["Ticket"] = Relationship(back_populates="board_status")
