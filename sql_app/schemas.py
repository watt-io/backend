from typing import Optional
from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    description: str
    
    class Config:
        orm_mode = True


class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    
    class Config:
        orm_mode = True

