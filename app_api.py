from fastapi import FastAPI
from pydantic import BaseModel
import json
from cria_json import Json_manager
from filmes_CRUD import Crud


db = Json_manager()
db.cria_json('db.json')
crud = Crud()
app = FastAPI()

@app.get('/')
def home():
    return {"Ino": "watt"}

@app.get('/filmes')
def mostra_filmes():
    return crud.read()

@app.get('/filmes/{id_filme}')
def mostra_filmes_id(id_filme: int):
    return crud.read_by_id(id_filme)

@app.post('/filmes')
def cria_filme(id: int, nome: str, ano: int, genero: str, duracao: str):
    crud.create(id, nome, ano, genero, duracao)
    return True

@app.delete('/filmes/{id_filme}')
def exclui_filme(id_filme: int):
    return crud.delete(id_filme)
    