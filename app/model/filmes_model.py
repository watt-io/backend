from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from app.db.database import *


# Definindo o modelo de dados do filme
class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    lancamento = Column(Integer)


# Criando classe de modelo para receber dados de entrada no POST
class FilmeCreate(BaseModel):
    titulo: str
    lancamento: int
