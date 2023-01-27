from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# Client DB model
class ClientDBModel(Base):
    __tablename__ = 'Clientes'
    
    id = Column(Integer, primary_key = True, index = True)
    movie_id = Column(Integer, ForeignKey('Filmes.id'), default= None)
    name = Column(String)
    premiumAccount = Column(Boolean)
    Adress = Column(String)
    filme = relationship('MovieDBModel', back_populates= 'rentedBy')

# Movie DB model
class MovieDBModel(Base):
    __tablename__ = 'Filmes'
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    length = Column(String)
    genre = Column(String)
    release = Column(Integer)
    rentedBy = relationship('ClientDBModel', back_populates='filme')