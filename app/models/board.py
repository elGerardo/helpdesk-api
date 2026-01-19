from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Board(SQLModel, table=True):
    __tablename__ = "boards"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    workspace_id: int = Field()
    name: str = Field()
    nomenclature: str = Field()
    description: Optional[str] = Field(default=None)
    logo: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)
