from sqlalchemy import Column, Integer, String
from .database import Base

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ano = Column(Integer)
    categoria = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)

