from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    name: str | None = None
    email: EmailStr | None = None
