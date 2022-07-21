from fastapi import FastAPI
from cria_json import Json_manager
from filmes_CRUD import Crud, Filme
from enum import Enum


class FilmeEnum(str, Enum):
    nome = "nome"
    ano = "ano"
    genero = "genero"
    duracao = "duracao"

db = Json_manager()
db.cria_json('db.json')
crud = Crud()
app = FastAPI(title='WattFlix++', description='API de filmes, desenvolvido por André Gomides')

@app.get('/')
async def home():
    return {"Ino": "watt"}

@app.get('/filmes')
async def mostra_filmes():
    return crud.read()

@app.get('/filmes/{id_filme}')
async def mostra_filmes_id(id_filme: str):
    return crud.read_by_id(id_filme)

@app.post('/filmes')
async def cria_filme(id: str, nome: str, ano: int, genero: str, duracao: str):
    crud.create(id, nome, ano, genero, duracao)
    return True

@app.delete('/filmes/{id_filme}')
async def exclui_filme(id_filme: str):
    return crud.delete(id_filme)

@app.put('/filmes/{id_filme}')
async def atualiza_filme(id_filme: str, campo: FilmeEnum, conteudo):
    return crud.update(id_filme, campo, conteudo)
    