from sqlmodel import Field, SQLModel

class TicketResponsible(SQLModel, table=True):
    __tablename__ = "ticket_responsibles"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    ticket_id: int = Field(foreign_key="tickets.id", primary_key=True)
    tenant_id: int = Field(primary_key=True)

    #user: Optional["User"] = Relationship(back_populates="ticket_responsibles")
    #ticket: Optional["Ticket"] = Relationship(back_populates="user_links")