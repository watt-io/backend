from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class MovieORM(Base):
    __tablename__ = "movies"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    duration = Column(String, nullable=False)  