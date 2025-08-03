from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MovieBase(BaseModel):
    title: str
    year: Optional[int] = None
    director: Optional[str] = None
    genre: Optional[str] = None
    synopsis: Optional[str] = None
    duration: Optional[int] = None
    rating: Optional[float] = None


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    director: Optional[str] = None
    genre: Optional[str] = None
    synopsis: Optional[str] = None
    duration: Optional[int] = None
    rating: Optional[float] = None


class Movie(MovieBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
