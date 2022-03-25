import pydantic as _pydantic


class _FilmeBase(_pydantic.BaseModel):
    nome: str
    diretor: str
    ano: int


class FilmeCreate(_FilmeBase):
    pass


class Filme(_FilmeBase):
    id: int

    class Config:
        orm_mode = True
