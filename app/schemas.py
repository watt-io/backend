from typing import Optional
from pydantic import BaseModel

class Movie(BaseModel):
    __tablename__ = 'filmes'

    title: str
    director: str
    duration: str
    release_year: int
    country_of_origin: str
    overview: Optional[str]
    budget: Optional[str]
    rating: Optional[str]
    genre: str
    starring: str
