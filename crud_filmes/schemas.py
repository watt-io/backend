from typing import  Optional
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
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    
    class Config():
        orm_mode = True

class ShowAllFilme(BaseModel):
    nome: str
    ano: int
    categoria: str
    id: int
    
    creator: ShowUser
    
    class Config():
        orm_mode = True

class ShowFilme(BaseModel):
    nome: str
    ano: int
    categoria: str
    
    creator: ShowUser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None