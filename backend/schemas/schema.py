from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_name: str


class MovieAdd(MovieBase):
    class Config:
        orm_mode = True


class Movie(MovieAdd):
    id: int
    class Config:
        orm_mode = True


class UpdateMovie(BaseModel):
    movie_name: str
    class Config:
        orm_mode = True
