from db_handler import Base
from sqlalchemy import Column, Integer, String


class Movies(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    movie_name = Column(String(255), index=True, nullable=False)
