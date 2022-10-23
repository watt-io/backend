from sqlalchemy import Column, Integer, String
from database import Base

class Filme(Base):
    
    __tablename__ = "Filmes"

    id: int = Column(Integer, primary_key = True, index = True)
    titulo: str = Column(String(100), nullable=False)
