from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Form(SQLModel, table=True):
    __tablename__ = "forms"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field()
    form_id: Optional[int] = Field(default=None)
    board_id: int = Field()
    title: str = Field()
    nomenclature: str = Field()
    description: Optional[str] = Field(default=None)
    status: str = Field(default="DRAFT")  # DRAFT | PUBLISHED
    version: int = Field(default=1)
    created_by: int = Field()
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)
