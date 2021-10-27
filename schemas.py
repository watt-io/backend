from pydantic import BaseModel

class Filme(BaseModel):
    id: int
    titulo: str
    ano: int
    duracao: int

    class Config:         
        orm_mode = True

lista = [] #lista de filmes retornada no response_model
