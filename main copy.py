from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Filme(BaseModel):
    id: int
    nome: str
    duracao: float
    avaliacao: float

lista_filmes = []

@app.get('/')
def root():
    return{"Hello"}

@app.get('/filmes')
def listar_filmes():
    return lista_filmes

@app.get("/filmes/{id}")
def filme_id(id: int):
    for filme in lista_filmes:
        if filme.id == id:
            return filme
    raise HTTPException(status_code=404, detail="Filme não encontrado")

@app.post('/filmes')
def criar_filme(filme: Filme):
    lista_filmes.append(filme)
    return {"Filme adicionado"}