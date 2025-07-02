from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
    genre = Column(String(50), nullable=False)
