from sqlalchemy import Column, Integer, String

from app.database import Base


class Filme(Base):
    """Modelo representando o catálogo de filmes na tabela 'filmes'."""
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    diretor = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)


