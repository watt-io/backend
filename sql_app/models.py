from sqlalchemy import Column, Integer, String

from .database import Base


class Movie(Base):
    __tablename__ = "filmes"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    descricao: str = Column(String(255), nullable=False)
    avaliacao: int = Column(Integer, nullable=False)
