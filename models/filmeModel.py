from pydantic import BaseModel

class FilmeModel(BaseModel):
    id: int
    titulo: str
    diretor: str
    ano_lancamento: int
    genero: str