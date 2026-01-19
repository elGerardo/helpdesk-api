from sqlmodel import Field, SQLModel

class UserBoard(SQLModel, table=True):
    __tablename__ = "users_boards"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    workspace_id: int = Field(primary_key=True)
    board_id: int = Field(primary_key=True)
    tenant_id: int = Field(primary_key=True)
