from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    year: int
    genre: str

class MovieData(BaseModel):
    id: int
    title: str
    year: int
    genre: str