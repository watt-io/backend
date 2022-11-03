from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    year: int
    genre: str
    director: str
    synopsis: str


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
