from pydantic import BaseModel

class FilmeBase(BaseModel):
    titulo: str
    ano: int
    duracao: int
    diretor: str

class FilmeCreate(FilmeBase):
    pass

class FilmeOut(FilmeBase):
    id: int

    class Config:
        from_attributes = True