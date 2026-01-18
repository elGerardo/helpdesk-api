from sqlmodel import Field, SQLModel
from typing import Optional, Dict
from datetime import datetime
from sqlalchemy import JSON, Column


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"

    id: int | None = Field(default=None, primary_key=True)
    row: int = Field()
    table: str = Field()
    generated_by: int = Field(foreign_key="users.id")
    deliveried_to: int = Field(foreign_key="users.id")
    meta: Optional[Dict] = Field(default=None, sa_column=Column(JSON))
    is_seen: bool = Field(default=False)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)
