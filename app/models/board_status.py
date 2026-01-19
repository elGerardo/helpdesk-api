from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

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
