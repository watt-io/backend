import json
from fastapi import FastAPI
from pydantic import BaseModel
import backend.dataBase as db

app = FastAPI()



@app.get("/filmes")
def mostra_filmes():
    filmes = db.ler_filmes()
    return filmes

@app.post("/filmes/{titulo}/{ano}")
def inserir_filmes(titulo, ano):
    inserido = db.inserir_filmes(titulo, ano)
    return inserido

@app.get("/filmes/{id}")
def busca_filmes(id):
    filme = db.filme_especifico(id)
    return filme
