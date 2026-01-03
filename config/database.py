from sqlmodel import create_engine, Session
import os
from sqlmodel import create_engine, Session
from typing import Annotated
from fastapi import Depends

from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"

engine = create_engine(DATABASE_URL, 
    echo=True,     
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,
    max_overflow=10
)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
