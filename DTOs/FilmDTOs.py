from pydantic import BaseModel, Field

class FilmBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Título do filme")
    synopsis: str = Field(None, max_length=500, description="Sinopse do filme")
    duration: int = Field(..., gt=0, le=600, description="Duração em minutos (até 10h)")
    language: str = Field(..., min_length=2, max_length=20, description="Idioma do filme")
    release_year: int = Field(..., ge=1900, le=2100, description="Ano de lançamento")
    rating: float = Field(None, ge=0, le=10, description="Classificação do filme (0-10)")
    category_id: int = Field(...,ge=1, description="ID da categoria")
    director_id: int = Field(...,ge=1, description="ID do diretor")

class FilmCreate(FilmBase):
    pass

class FilmResponse(FilmBase):
    id: int

    class Config:
        orm_mode = True
