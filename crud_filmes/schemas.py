from pydantic import BaseModel

class Filme(BaseModel):
    nome: str
    ano: int
    categoria: str