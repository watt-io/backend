from pydantic import BaseModel

class Filmes(BaseModel):
    nome: str
    ano: int
    genero: str
    class Config:
        schema_extra = {
            "example": {
                "nome": "Matrix",
                "ano": 1999,
                "genero": "Ação"
            }
        }
class FilmesResponse(Filmes):
    id: int
    class Config:
        orm_mode = True 

class FilmesRequest(Filmes):
    ... 
