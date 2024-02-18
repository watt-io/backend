import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
engine = sqlalchemy.create_engine('sqlite:///filmes.db', echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    titulo = Column(String(50), nullable=True)
    ano = Column(Integer(), nullable=True)
    genero = Column(String(15), nullable=True)

Base.metadata.create_all(engine)   
