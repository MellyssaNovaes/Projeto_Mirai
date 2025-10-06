from sqlmodel import create_engine
from sqlmodel import Session
from typing import Annotated
from fastapi import Depends
import os

db_url = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/postgres")

engine = create_engine(db_url)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]