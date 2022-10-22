from pydantic import BaseModel

class Filme(BaseModel):
    id:int
    nome:str
    genero:str
    diretor:str