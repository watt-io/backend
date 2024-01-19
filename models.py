from sqlalchemy import TIMESTAMP, Column, Integer, String
from database import Base


class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    genero = Column(String, index=True, nullable=True)
    ano = Column(Integer, index=True, nullable=True)
    descricao = Column(String, index=True, nullable=True)
