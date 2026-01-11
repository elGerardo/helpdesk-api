from sqlmodel import Field, SQLModel, select, Relationship
from config.database import get_session
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

# Import TicketResponsible outside TYPE_CHECKING for link_model
from app.models.ticket_responsible import TicketResponsible

if TYPE_CHECKING:
    from app.models.ticket import Ticket

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    name: str = Field(index=True)
    last_name: str = Field(index=True)
    user_name: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    profile_image: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)

    #ticket_responsibles: Optional[List["TicketResponsible"]] = Relationship(
    #    back_populates="user")
    
    tickets: Optional[List["Ticket"]] = Relationship(
        back_populates="users",
        link_model=TicketResponsible
    )

    _query = None
    _session = None
    def query(self) -> select:
        if not self._session:
            self._session = next(get_session())
        if not self._query:
            self._query = select(User)
        return self

    def first(self, query):
        result = self._session.exec(query).first()
        return result

    def create(self):
        if not self._session:
            self._session = next(get_session())
        #self.created_at = 'now()'
        #self.updated_at = 'now()'
        self._session.add(self)
        self._session.commit()
        self._session.refresh(self)
        return self