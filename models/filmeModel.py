from pydantic import BaseModel, Field

class FilmeModel(BaseModel):
    titulo: str = Field(max_length=255)
    diretor: str = Field(max_length=255)
    ano_lancamento: int
    genero: str = Field(max_length=255)

class FilmeResponse(FilmeModel):
    id: int