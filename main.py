from fastapi import FastAPI
from utils.db import mySqlDb
from controllers.filmeController import FilmeController
from services.connectionService import determinar_conexao

app = FastAPI()

repo = determinar_conexao()
item_controller = FilmeController(repo)

app.include_router(item_controller.router)

@app.get("/")
def root():
    """
    Rota raiz que redireciona para a documentação da API.
    """
    return {"message": "Acesse a documentação da API em /docs"}
