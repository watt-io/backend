from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    duracao = Column(Integer, nullable=False)
    diretor = Column(String)