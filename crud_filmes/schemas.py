from pydantic import BaseModel

class Filme(BaseModel):
    id: int
    nome: str
    ano: int
    categoria: str