from sqlalchemy import Column, Integer, String, DateTime, func, Date, event

from movies.infrastructure.database.models.base import Base
from movies.infrastructure.database.models.helpers.helpers import generate_data


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    release_year = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


event.listen(Movies, 'before_insert', generate_data)
