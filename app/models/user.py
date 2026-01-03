from sqlmodel import Field, SQLModel, select
from config.database import get_session

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    last_name: str = Field(index=True)
    user_name: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    created_at: str = Field(default=None)
    updated_at: str = Field(default=None)
    deleted_at: str = Field(default=None)

    _query = None
    _session = None
    def query(self) -> select:
        if not self._session:
            self._session = next(get_session())
        if not self._query:
            self._query = select(User)
        return self

    def first(self, query):
        result = self._session.exec(query).first()
        return result

    def create(self):
        if not self._session:
            self._session = next(get_session())
        #self.created_at = 'now()'
        #self.updated_at = 'now()'
        self._session.add(self)
        self._session.commit()
        self._session.refresh(self)
        return self