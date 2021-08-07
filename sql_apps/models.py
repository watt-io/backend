from sqlalchemy import Column, String
from sql_apps.database import Base


class MovieDb(Base):
    __tablename__ = "movies"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=False, default="Random Name")
    description = Column(String, unique=False, default="Random Description")
    duration = Column(String, unique=False, default="Random Duration")
    director = Column(String, unique=False, default="Random Director")
    release_date = Column(String, unique=False, default="Random Release Date")

    def __repr__(self):
        return f"{self.name}"
