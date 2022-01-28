from schemas import addFilmeSchema
from datetime import datetime
from multiprocessing import dummy
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Dict, List, Union, Generator
from sqlalchemy.orm import Session
from crud import (
    cria_filme,
    lista_todos_filmes,
    get_filme
)
from database import Base, SessionLocal, engine
from schemas import addFilmeSchema


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

# Descricao da documentacao
tags_metadata = [
    {
        "name": "estouFuncionando",
        "description": "Checa se a API está funcionando retornando uma string 'sim'",
    },
    {
        "name": "filmes",
        "description": "Retorna os filmes no bancos de dados ou insere novos filmes"
    }
]

app = FastAPI(title="InoWattflix API",
              description="Documentação das rotas de listagem e adição de filmes na InoWattFlix. Teste de admissão estágio em Python back-end.",
              version="1.0",
              contact={
                  "name": "Vinícius Zamariola",
                  "url": "https://github.com/Zamariolo/",
                  "email": "viniciuszamariola@gmail.com"
              },
              openapi_tags=tags_metadata)


@app.get("/estoufuncionando/", tags=["estouFuncionando"], response_model=str)
def estouFuncionando() -> Dict[str, datetime]:
    return "sim"


@app.get("/filmes", tags=['filmes'], status_code=status.HTTP_200_OK)
async def get_all_filmes(db: Session = Depends(get_db)):
    if result := lista_todos_filmes(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Nenhum filme encontrado",
    )


@app.get("/filmes/{id}/", tags=['filmes'], status_code=status.HTTP_200_OK)
def get_filme_especifico(id: int, db: Session = Depends(get_db)) -> Dict[str, Union[float, int, str]]:
    if response := get_filme(db, id):
        return response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} não encontrado.",
    )


def get_max() -> int:
    max_id_filme = max(listaFilmes, key=lambda i: i.get("id", 0))
    return max_id_filme.get("id", 0)


@app.post('/filmes/', tags=['filmes'], status_code=status.HTTP_201_CREATED)
def post_filme(filme: addFilmeSchema, db: Session = Depends(get_db),):
    if result := cria_filme(db, filme):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
