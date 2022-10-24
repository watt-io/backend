from sqlalchemy import Column, Integer, String
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    director = Column(String)
    duration = Column(String)
    release_year = Column(Integer)
    country_of_origin = Column(String)
    overview = Column(String)
    budget = Column(String)
    rating = Column(String)
    genre = Column(String)
    starring = Column(String)