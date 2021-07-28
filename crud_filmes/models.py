from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ano = Column(Integer)
    categoria = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="filmes")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)

    filmes = relationship("Filme", back_populates="creator")
