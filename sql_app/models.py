from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Movie(Base):
    __tablename__ = "filme"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    descreption = Column(String, unique=True)
