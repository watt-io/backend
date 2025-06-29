from pydantic import BaseModel

class Filme(BaseModel):
    id: int
    nome: str
    duracao: float
    avaliacao: float
    ano_lancamento: int
    diretor: str

    class Config:
        from_attributes = True
