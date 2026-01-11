from sqlmodel import Field, SQLModel, select
from pydantic import field_validator
from app.models.tenant import Tenant
from app.models.user import User
from config.database import get_session
from typing import Optional


class StoreTenantDTO(SQLModel):
    owner_id: Optional[int] = Field(default=None)
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=255)
    
    @field_validator('owner_id')
    @classmethod
    def validate_owner_exists(cls, value) -> Optional[int]:
        if value is not None:
            session = next(get_session())
            res = select(User).where(User.id == value)
            result = session.exec(res).first()
            if not result:
                raise ValueError('owner_id must reference an existing user')
        return value
