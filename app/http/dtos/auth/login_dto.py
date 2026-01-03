from sqlmodel import Field, SQLModel, select
from pydantic import field_validator
from app.models.user import User
from config.database import get_session

class LoginDTO(SQLModel):
    identifier: str = Field(min_length=1, max_length=256)
    password: str = Field(min_length=1, max_length=256)