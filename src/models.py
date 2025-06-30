from pydantic import BaseModel

class MovieModel(BaseModel):
    movie_name: str
    synopsis: str
    duration: int
    year_release: int
    movie_genre: str