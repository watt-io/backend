from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MovieBase(BaseModel):
    title: str
    director: str
    year: int
    synopsis: Optional[str] = None
    genre: Optional[str] = None


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = None
    synopsis: Optional[str] = None


class Movie(MovieBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
