from sqlmodel import Field, SQLModel, select
from pydantic import field_validator
from app.models.tenant import Tenant
from config.database import get_session
from typing import Optional


class StoreWorkspaceDTO(SQLModel):
    tenant_id: Optional[int] = Field()
    name: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=255)
    logo: Optional[str] = Field(default=None, max_length=255)
    color: str = Field(min_length=1, max_length=255)
    
    #@field_validator('tenant_id')
    #@classmethod
    #def validate_tenant_exists(cls, value) -> int:
    #    session = next(get_session())
    #    res = select(Tenant).where(Tenant.id == value)
    #    result = session.exec(res).first()
    #    if not result:
    #        raise ValueError('tenant_id must reference an existing tenant')
    #    return value
    
    @field_validator('name')
    @classmethod
    def validate_name_not_empty(cls, value) -> str:
        if not value or not value.strip():
            raise ValueError('name cannot be empty')
        return value.strip()
