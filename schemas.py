from pydantic import BaseModel


class FilmeBase(BaseModel):
    titulo: str
    diretor: str
    data_adicionado: str
    sinopse: str
    ano_lancamento: int
    duracao_min: int
    class_indicativa: str


class FilmeRequest(FilmeBase):
    ...


class FilmeResponse(FilmeBase):
    id: int

    class Config:
        orm_mode = True
