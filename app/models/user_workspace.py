from sqlmodel import Field, SQLModel


class UserWorkspace(SQLModel, table=True):
    __tablename__ = "users_workspaces"

    user_id: int = Field(primary_key=True)
    workspace_id: int = Field(primary_key=True)
    tenant_id: int = Field(primary_key=True)
