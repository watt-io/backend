# Modelos do pydantic para validacao de dados da API

from pydantic import BaseModel, validator


class filmesBaseSchema(BaseModel):
    nome: str
    nota_imdb: float
    family_friendly: bool

class getFilmesSchema(filmesBaseSchema):
    id: int


class addFilmeSchema(filmesBaseSchema):
    @validator("nota_imdb")
    def validate_nota_imdb(cls, v: float, **kwargs) -> float:
        if v < 0.0:
            raise ValueError("Nota do imdb não pode ser menor do que 0")
        elif v > 10:
            raise ValueError("Nota do imdb não pode ser maior do que 10")
        return v
