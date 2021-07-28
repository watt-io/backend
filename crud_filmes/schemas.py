from typing import List
from pydantic import BaseModel

class FilmeBase(BaseModel):
    nome: str
    ano: int
    categoria: str


class Filme(FilmeBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    password: str


class ShowUser(BaseModel):
    name: str
    filmes: List[Filme] = []
    
    class Config():
        orm_mode = True

class ShowFilme(BaseModel):
    nome: str
    ano: int
    categoria: str
    
    creator: ShowUser
    
    class Config():
        orm_mode = True