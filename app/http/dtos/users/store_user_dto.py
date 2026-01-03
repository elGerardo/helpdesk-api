from sqlmodel import Field, SQLModel, select
from pydantic import field_validator
from app.models.user import User
from config.database import get_session

class StoreUserDTO(SQLModel):
    name: str = Field(min_length=1, max_length=256)
    email: str = Field(regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    
    @field_validator('email')
    @classmethod
    def validate_unique_email(cls, value) -> str:
        session = next(get_session())
        res = select(User).where(User.email == value)
        result = session.exec(res).first()
        if result:
            raise ValueError('email must be unique')
        return value