from sqlalchemy import Column, Integer, String, Date
from Data.session import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True, index= True)
    name = Column(String, nullable=False)
    films = relationship("Film", back_populates="category")