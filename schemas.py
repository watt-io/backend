from pydantic import BaseModel


class FilmeBase(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int


class FilmeRequest(FilmeBase):
    ...


class FilmeResponse(FilmeBase):
    id: int

    class Config:
        orm_mode = True
