from sqlmodel import Field, SQLModel

class User(SQLModel, table=True): 
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str