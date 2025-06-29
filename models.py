from sqlalchemy import Column, Integer, String, Float, Sequence
from database import Base

class FilmeModel(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    duracao = Column(Float)
    avaliacao = Column(Float)
    ano_lancamento = Column(Integer)
    diretor = Column(String)