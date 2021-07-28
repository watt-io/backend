from crud_filmes.database import Base
from pydantic import BaseModel

class Filme(BaseModel):
    nome: str
    ano: int
    categoria: str

class ShowFilme(Filme):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    password: str

class ShowUser(BaseModel):
    name: str
    class Config():
        orm_mode = True
    