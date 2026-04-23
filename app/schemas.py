from pydantic import BaseModel

class FilmeCreate(BaseModel):
    titulo: str
    descricao: str

class FilmeResponse(FilmeCreate):
    id: int

    class Config:
        orm_mode = True