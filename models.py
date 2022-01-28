from sqlalchemy import Boolean, Column, Float, Integer, String
from database import Base

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    nota_imdb = Column(Float)
    family_friendly = Column(Boolean)