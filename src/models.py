from sqlalchemy import Column, Integer, String
from database import Base

class Filme(Base):
    __tablename__ = "filmes"
    id: int = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ano = Column(Integer)
    genero = Column(String)