from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)

    class Config:
        from_attributes = True  
