from pydantic import BaseModel
from typing import Optional

class FilmeBase(BaseModel):
    titulo: str
    diretor: str
    ano: int

class FilmeCreate(FilmeBase):
    pass

class Filme(FilmeBase):
    id: int

    class Config:
        from_attributes = True