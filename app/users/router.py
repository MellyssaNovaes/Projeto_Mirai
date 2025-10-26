from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from app.users.model import User, UserCreate, UserRead, UserUpdate 
from app.engine import SessionDep

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, session: SessionDep):
    """Cria um novo usuário, verificando se o e-mail é único."""
    
    existing_user_statement = select(User).where(User.email == user.email)
    existing_user = session.exec(existing_user_statement).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="O e-mail fornecido já está cadastrado."
        )
    
    db_user = User.model_validate(user)
    
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user

@user_router.get("/", response_model=list[UserRead])
def read_all_users(session: SessionDep, skip: int = 0, limit: int = 100):
    """Busca e retorna uma lista de todos os usuários cadastrados. Adiciona Paginação (skip para pular, limit para o máximo de itens)."""
    
    statement = select(User).offset(skip).limit(limit)
    
    results = session.exec(statement)
    users = results.all()
    
    return users

@user_router.get("/{user_id}", response_model=UserRead)
def read_user_by_id(user_id: int, session: SessionDep):
    """Busca um usuário específico pelo ID."""
    
    user = session.get(User, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return user

@user_router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate, session: SessionDep):
    """Atualiza um ou mais campos de um usuário existente."""

    db_user = session.get(User, user_id)
    
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if user_update.email:
        existing_user_statement = select(User).where(User.email == user_update.email)
        existing_user = session.exec(existing_user_statement).first()
        
        if existing_user and existing_user.id != user_id:
             raise HTTPException(
                status_code=409,
                detail="O novo e-mail fornecido já está cadastrado em outro usuário."
            )
        
    update_data = user_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_user, key, value)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user

@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, session: SessionDep):
    """Remove um usuário existente pelo ID."""

    user = session.get(User, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    session.delete(user)
    session.commit()
    
    return