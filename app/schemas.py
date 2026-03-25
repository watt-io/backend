from pydantic import BaseModel, ConfigDict, Field


class FilmeBase(BaseModel):
    """Campos base para validação de filmes."""
    titulo: str = Field(
        ...,
        min_length=1,
        max_length=200,
        examples=["O Poderoso Chefão"],
        description="Título do filme"
    )
    diretor: str = Field(
        ...,
        min_length=1,
        max_length=100,
        examples=["Francis Ford Coppola"],
        description="Nome do diretor"
    )
    ano: int = Field(
        ...,
        ge=1888,
        le=2030,
        examples=[1972],
        description="Ano de lançamento (entre 1888 e 2030)"
    )
    genero: str = Field(
        ...,
        min_length=1,
        max_length=50,
        examples=["Drama"],
        description="Gênero do filme"
    )


class FilmeCreate(FilmeBase):
    pass


class FilmeUpdate(BaseModel):
    """Esquema para atualização parcial de um filme."""
    titulo: str | None = Field(
        None, min_length=1, max_length=200, description="Título do filme"
    )
    diretor: str | None = Field(
        None, min_length=1, max_length=100, description="Nome do diretor"
    )
    ano: int | None = Field(
        None, ge=1888, le=2030, description="Ano de lançamento"
    )
    genero: str | None = Field(
        None, min_length=1, max_length=50, description="Gênero do filme"
    )


class FilmeResponse(FilmeBase):
    """Esquema de resposta incluindo o ID do banco de dados."""
    model_config = ConfigDict(from_attributes=True)

    id: int


