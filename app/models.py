from sqlalchemy import Column, Integer, String
from .database import Base

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False)
    diretor = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
