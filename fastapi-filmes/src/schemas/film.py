from pydantic import BaseModel

class FilmBase(BaseModel):
    title: str
    director: str
    year: int

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    id: int

    class Config:
        orm_mode = True
