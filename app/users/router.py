from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.users.model import User, UserCreate, UserRead  
from app.engine import SessionDep 

user_router = APIRouter()

@user_router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: SessionDep):
    
    db_user = User.model_validate(user)
    
    session.add(db_user)
    session.commit()
    session.refresh(db_user)  
    
    return db_user

# NOVAS ROTAS GET 

@user_router.get("/", response_model=list[UserRead])
def read_all_users(session: SessionDep):
    
    statement = select(User)
    
    results = session.exec(statement)
    
    users = results.all()
    
    return users

@user_router.get("/{user_id}", response_model=UserRead)
def read_user_by_id(user_id: int, session: SessionDep):
    
    user = session.get(User, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return user