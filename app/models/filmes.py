from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.database import base


class Filme(base):
    __tablename__ = "filmes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    titulo: Mapped[str]
    descricao: Mapped[str]
    ano: Mapped[int]
    genero: Mapped[str]
    diretor: Mapped[str]
    atores: Mapped[list[str]] = mapped_column(ARRAY(String))
    url_trailer: Mapped[str]
    classificacao_etaria: Mapped[str]
