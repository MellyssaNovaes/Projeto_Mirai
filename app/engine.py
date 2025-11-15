import logging
import os
from typing import Annotated

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, SQLModel, create_engine

db_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/postgres")

try:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        pass
except SQLAlchemyError as e:
    logging.error(f"Erro ao conectar ao banco de dados: {e}")
    raise


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
