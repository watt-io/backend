from pydantic import BaseModel

class FilmeBase(BaseModel):
    titulo: str
    diretor: str
    ano: int
    genero: str

class FilmeCreate(FilmeBase):
    pass

class FilmeUpdate(FilmeBase):
    pass

class FilmeResponse(FilmeBase):
    id: int

    class Config:
        from_attributes = True