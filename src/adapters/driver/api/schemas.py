from pydantic import BaseModel
from typing import Optional

class MovieCreate(BaseModel):
    title: str
    year: int
    duration: str

class MovieRead(BaseModel):
    id: str
    title: str
    year: int
    duration: str

    class Config:
        orm_mode = True