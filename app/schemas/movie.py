from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    director: str
    year: int

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

    class Config:
        from_attributes = True
