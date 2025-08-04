from fastapi import HTTPException
from sqlalchemy import select

from app.database import session_local
from app.models.filmes import Filme as FilmeDBModel
from app.schemas.filmes import Filme as FilmeSchema

db = session_local()


async def create_filme(filme_data: FilmeSchema) -> FilmeDBModel:
    """
    Cria um novo filme no banco de dados
    """
    db_filme = FilmeDBModel(
        titulo=filme_data.titulo,
        descricao=filme_data.descricao,
        ano=filme_data.ano,
        genero=filme_data.genero,
        diretor=filme_data.diretor,
        atores=filme_data.atores,
        url_trailer=str(filme_data.url_trailer),
        classificacao_etaria=filme_data.classificacao_etaria,
    )

    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)

    return db_filme


async def get_filmes() -> list[FilmeDBModel]:
    if not (filmes := db.scalars(select(FilmeDBModel)).all()):
        raise HTTPException(status_code=404, detail="Filmes não encontrados.")
    return filmes


async def get_filme(filme_id: int):
    if not (
        filme := db.scalars(
            select(FilmeDBModel).where(FilmeDBModel.id == filme_id)
        ).first()
    ):
        raise HTTPException(status_code=404, detail=f"Filme {filme_id} não encontrado.")
    return filme
