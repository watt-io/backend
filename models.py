from sqlalchemy import Column, Integer, String

from db import Base

#Criação do modelo Filme para o banco de dados
class Filme(Base):
    __tablename__ = "filmes"

    id: int = Column(Integer, primary_key=True, index=True)
    type: str = Column(String(50))
    title: str = Column(String(100), nullable=False)
    director: str = Column(String(100), nullable=False)
    description: str = Column(String(300), nullable=False)
    