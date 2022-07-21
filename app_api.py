from fastapi import FastAPI
import json
from cria_json import Json_manager
from filmes_CRUD import Crud, Filme


db = Json_manager()
db.cria_json('db.json')
crud = Crud()
app = FastAPI(title='WattFlix++')

@app.get('/')
def home():
    return {"Ino": "watt"}

@app.get('/filmes')
def mostra_filmes():
    return crud.read()

@app.get('/filmes/{id_filme}')
def mostra_filmes_id(id_filme: str):
    return crud.read_by_id(id_filme)

@app.post('/filmes')
def cria_filme(id: str, nome: str, ano: int, genero: str, duracao: str):
    crud.create(id, nome, ano, genero, duracao)
    return True

@app.delete('/filmes/{id_filme}')
def exclui_filme(id_filme: str):
    return crud.delete(id_filme)

@app.put('/filmes/{id_filme}')
def atualiza_filme(id_filme: str, oq_mudar: str, conteudo_desejado):
    """ 
        No campo oq_mudar digite: nome, ano, genero ou duracao!! DIGITE EXATAMENTE DESSA FORMA!
    """
    return crud.update(id_filme, oq_mudar, conteudo_desejado)
    