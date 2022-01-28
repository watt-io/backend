from datetime import datetime
from multiprocessing import dummy
from typing import Dict
from fastapi import FastAPI, HTTPException, status
from typing import Dict, List, Optional, Union
# from fastapi_pagination import Page, add_pagination, paginate

# Dummy imports
import json
dummyDB = json.load(open("dummyDatabase.json", "r"))

# Descricao da documentacao
tags_metadata = [
    {
        "name": "seraQueEstouFuncionando",
        "description": "Checa se a API está funcionando retornando uma string 'sim'",
    },
    {
        "name": "filmes",
        "description": "Retorna os filmes no bancos de dados ou insere novos filmes"
    }
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/seraQueEstouFuncionando/", tags=["seraQueEstouFuncionando"])
def amIWorking() -> Dict[str, datetime]:
    return "sim"


@app.get("/filmes", tags=['filmes'])
def get_all_filmes() -> List[Dict[str, Union[float, int, str, bool]]]:
    if response := dummyDB:
        return response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Nenhum filme encontrado"
    )

@app.get("/filmes/{id}/", tags=['filmes'])
def get_filme(id: int) -> Dict[str, Union[float, int, str, bool]]:
    if response := list(
        filter(lambda i: i.get("id") == id, dummyDB)
    ):
        return response[0]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} não encontrado.",
    )


# add_pagination(app)