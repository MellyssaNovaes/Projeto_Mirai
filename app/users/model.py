from typing import Optional
from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserRead(UserBase):
    id: int