from typing import Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import engine, get_db

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
        filmes = db.query(models.Filme).all()
        return {"data": filmes}
    except Exception as e:
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
        filme = db.query(models.Filme).filter(models.Filme.id == id).first()
        if not filme:
            return {"error": "Filme não encontrado!"}
        return {"data": filme}
    except Exception as e:
        return {"message": "Erro ao buscar filme"}


@app.post("/filmes")
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
        db.add(new_filme)
        db.commit()
        db.refresh(new_filme)

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
        filme = db.query(models.Filme).filter(models.Filme.id == id).first()
        if not filme:
            return {"error": "Filme não encontrado!"}
        if filme_modificado.nome:
            filme.nome = filme_modificado.nome
        if filme_modificado.ano:
            filme.ano = filme_modificado.ano
        if filme_modificado.genero:
            filme.genero = filme_modificado.genero
        if filme_modificado.descricao:
            filme.descricao = filme_modificado.descricao
        db.commit()
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
        filme = db.query(models.Filme).filter(models.Filme.id == id).first()
        db.delete(filme)
        db.commit()

        return {"message": "Filme deletado com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar filme"}
