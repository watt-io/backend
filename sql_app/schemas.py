from pydantic import BaseModel


class MovieBase(BaseModel):
    titulo: str
    descricao: str
    avaliacao: int


class MovieRequest(MovieBase):
    ...


class MovieResponse(MovieBase):
    id: int

    class Config:
        orm_mode = True
