from pydantic import BaseModel

class Filme(BaseModel):
    nome: str
    ano: int
    categoria: str

class ShowFilme(Filme):
    class Config():
        orm_mode = True