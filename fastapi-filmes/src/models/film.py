from sqlalchemy import Column, Integer, String
from src.db.database import Base

class FilmModel(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String, index=True)
    year = Column(Integer)
