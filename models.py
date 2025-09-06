from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    diretor = Column(String)
    ano = Column(Integer)

class FilmeCreate(BaseModel):
    titulo: str
    diretor: str
    ano: int

class FilmeRead(FilmeCreate):
    id: int
    class Config:
        orm_mode = True
