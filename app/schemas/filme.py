from pydantic import BaseModel, ConfigDict, Field


class FilmeCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)
    diretor: str = Field(..., min_length=1, max_length=255)
    ano: int = Field(..., ge=1888, le=2100)
    genero: str = Field(..., min_length=1, max_length=100)
    sinopse: str = Field(..., min_length=1)


class FilmeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    diretor: str
    ano: int
    genero: str
    sinopse: str
