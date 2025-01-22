from fastapi import FastAPI
from utils.db import mySqlDb
from controllers.filmeController import FilmeController
from models.repos.filmeRepoMySQL import FilmeRepoMySQL

app = FastAPI()

connectionMySql = mySqlDb.criar_conexao_mySql()
repoMySql = FilmeRepoMySQL(connectionMySql)
item_controller = FilmeController(repoMySql)

app.include_router(item_controller.router)

