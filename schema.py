from turtle import title
from pydantic import BaseModel

class FilmeBase(BaseModel):
    title: str
    type: str
    director: str
    description: str

class FilmeRequest(FilmeBase):
    ...

class FilmeResponse(FilmeBase):
    id: int

    class Config:
        orm_mode = True