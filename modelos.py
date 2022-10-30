from sqlalchemy import Column, Integer, String
from database import Base
# Modelo para classe de Filmes


class Filme(Base):
    __tablename__ = "filmes"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    diretor: str = Column(String(30), nullable=True)
    data_adicionado: str = Column(String(20), nullable=False)
    sinopse: str = Column(String(255), nullable=False)
    ano_lancamento: int = Column(Integer, nullable=False)
    duracao_min: int = Column(Integer, nullable=False)
    class_indicativa: str = Column(String(5), nullable=False)
