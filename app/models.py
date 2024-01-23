from sqlalchemy import Column, Integer, String

from app.database import Base


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    director = Column(String)
    year = Column(Integer)