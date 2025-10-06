from fastapi import APIRouter
from sqlmodel import Session
from .model import User
from app.engine import SessionDep

user_router = APIRouter()

@user_router.post("/users/")
def create_user(nome: str, email: str, session: SessionDep) -> User:
    user = User(nome=nome, email=email)
    session.add(user)
    session.commit()
    return user
