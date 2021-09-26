# Import all types we'll be using to create table of 'Movies' class
from sqlalchemy import Column, Integer, String
# From database.py file, import Base
from database import Base

class MoviesTable(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    year = Column(Integer)
