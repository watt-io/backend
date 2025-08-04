from pydantic import AnyUrl, BaseModel


class Filme(BaseModel):
    id: int
    titulo: str
    descricao: str
    ano: int
    genero: str
    diretor: str
    atores: list[str]
    url_trailer: AnyUrl
    classificacao_etaria: str

    class Config:
        orm_mode = True
