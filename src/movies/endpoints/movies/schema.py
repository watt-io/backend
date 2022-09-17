from datetime import datetime

from pydantic import BaseModel


class MovieSchema(BaseModel):
    name: str
    description: str
    release_year: str


class MoviesSchema(BaseModel):
    id: int
    name: str
    description: str
    release_year: str
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateMovieSchema(BaseModel):
    name: str = None
    description: str =  None
    release_year: str = None


