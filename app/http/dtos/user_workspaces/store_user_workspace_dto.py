from sqlmodel import Field, SQLModel, select
from pydantic import field_validator
from app.models.user import User
from app.models.workspace import Workspace
from app.models.tenant import Tenant
from config.database import get_session


class StoreUserWorkspaceDTO(SQLModel):
    user_id: int = Field()
    workspace_id: int = Field()
    tenant_id: int = Field()
    
    #@field_validator('user_id')
    #@classmethod
    #def validate_user_exists(cls, value) -> int:
    #    session = next(get_session())
    #    res = select(User).where(User.id == value)
    #    result = session.exec(res).first()
    #    if not result:
    #        raise ValueError('user_id must reference an existing user')
    #    return value
    
    #@field_validator('workspace_id')
    #@classmethod
    #def validate_workspace_exists(cls, value) -> int:
    #    session = next(get_session())
    #    res = select(Workspace).where(Workspace.id == value)
    #    result = session.exec(res).first()
    #    if not result:
    #        raise ValueError('workspace_id must reference an existing workspace')
    #    return value
    
    #@field_validator('tenant_id')
    #@classmethod
    #def validate_tenant_exists(cls, value) -> int:
    #    session = next(get_session())
    #    res = select(Tenant).where(Tenant.id == value)
    #    result = session.exec(res).first()
    #    if not result:
    #        raise ValueError('tenant_id must reference an existing tenant')
    #    return value
