from datetime import datetime
from multiprocessing import dummy
from typing import Dict
from fastapi import Depends, FastAPI, HTTPException, Response, status
from typing import Dict, List, Union, Generator
from sqlalchemy.orm import Session
from crud import (
    cria_filme,
    lista_todos_filmes,
)
from database import Base, SessionLocal, engine
from schemas import filmesBaseSchema, addFilmeSchema
# from fastapi_pagination import Page, add_pagination, paginate

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

# Dummy imports
import json

from schemas import addFilmeSchema
listaFilmes = json.load(open("dummyDatabase.json", "r"))

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

app = FastAPI(title="InnoWatflix API",
              description="Documentação das rotas de listagem e adição de filmes na InnoWatFlix. Teste de admissão estágio em Python back-end.",
              version="1.0",
              contact={
                  "name": "Vinícius Zamariola",
                  "url": "https://github.com/Zamariolo/",
                  "email": "viniciuszamariola@gmail.com"
              },
              openapi_tags=tags_metadata)


@app.get("/estoufuncionando/", tags=["estouFuncionando"])
def estouFuncionando() -> Dict[str, datetime]:
    return "sim"


@app.get("/filmes", tags=['filmes'], status_code=status.HTTP_200_OK)
def get_all_filmes(db: Session = Depends(get_db)) -> List[Dict[str, Union[float, int, str, bool]]]:
    if result := lista_todos_filmes(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Nenhum filme encontrado",
    )


@app.get("/filmes/{id}/", tags=['filmes'])
def get_filme(id: int) -> Dict[str, Union[float, int, str, bool]]:
    if response := list(
        filter(lambda i: i.get("id") == id, listaFilmes)
    ):
        return response[0]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} não encontrado.",
    )


def get_max() -> int:
    max_id_filme = max(listaFilmes, key=lambda i: i.get("id", 0))
    return max_id_filme.get("id", 0)


@app.post('/filmes/', tags=['filmes'], status_code=status.HTTP_201_CREATED,)
def post_filme(filme: addFilmeSchema, db: Session = Depends(get_db),):
    if result := cria_filme(db, filme):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


# add_pagination(app)
