from sqlalchemy import Column, Integer, String

from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    genre = Column(String)
    director = Column(String)
    synopsis = Column(String)
