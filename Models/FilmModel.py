from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from Data.session import Base

class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    synopsis = Column(String, nullable=True)
    duration = Column(Integer, nullable=False)  # duração em minutos
    language = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=True)  # classificação do filme (ex: IMDb)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)

    category = relationship("Category", back_populates="films")
    director = relationship("Director", back_populates="films")