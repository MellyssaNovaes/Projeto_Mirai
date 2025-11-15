from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import EmailStr

class UserBase(SQLModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserRead(UserBase):
    id: int

class UserUpdate (UserBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None