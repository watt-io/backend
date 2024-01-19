from typing import Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import models
from database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Filme(BaseModel):
    nome: str
    ano: Optional[int]
    genero: Optional[str]
    descricao: Optional[str]


@app.get("/filmes")
async def root(db: Session = Depends(get_db)):
    """Retorna todos os filmes cadastrados no banco de dados

    Returns:
        [dict]: {"data": [Filme]}
    """
    try:
        filmes = models.Filme.listar(db=db)
        return {"data": filmes}
    except Exception as e:
        breakpoint()
        return {"message": "Erro ao buscar filmes"}


@app.get("/filmes/{id}")
async def get_movie(id: int, db: Session = Depends(get_db)):
    """Retorna um filme específico

    Args:
        id (int): id do filme

    Returns:
        filme: Filme
    """
    try:
        filme = models.Filme.buscar(filme_id=id, db=db)
        return {"data": filme}
    except Exception as e:
        return {"message": "Erro ao buscar filme"}


@app.post("/filmes", status_code=201)
async def create_movie(filme: Filme, db: Session = Depends(get_db)):
    """cria um novo filme

    Args:
        filme (Filme): Novo filme

    Returns:
        str: mensagem de sucesso ou erro
    """
    try:
        new_filme = models.Filme(
            nome=filme.nome,
            ano=filme.ano,
            genero=filme.genero,
            descricao=filme.descricao,
        )
        models.Filme.criar(filme=new_filme, db=db)

        return {"message": "Filme criado com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao criar filme"}


@app.put("/filmes/{id}")
async def update_movie(id: int, filme_modificado: Filme, db: Session = Depends(get_db)):
    """atualiza um filme

    Args:
        id (int): atualiza o filme com o id
        filme_modificado (Filme): novos valores para colocar no fime

    Returns:
        _type_: _description_
    """
    try:
        models.Filme.atualizar(filme_id=id, filme_modificado=filme_modificado, db=db)
        return {"message": "Filme atualizado com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao atualizar filme"}


@app.delete("/filmes/{id}")
async def delete_movie(id: int, db: Session = Depends(get_db)):
    """deleta um filme

    Args:
        id (int): id do filme a ser deletado

    Returns:
        str: mensagem de sucesso ou erro
    """
    try:
        models.Filme.deletar(filme_id=id, db=db)

        return {"message": "Filme deletado com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar filme"}
