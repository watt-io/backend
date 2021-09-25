# Projeto API REST para um catálogo de filmes
# Autor :  Gabriel Orlando Campista Petrucci
# Projeto realizado utilizando a documentação em https://fastapi.tiangolo.com/tutorial

from fastapi import FastAPI
from sqlalchemy.orm import Session
from starlette.requests import Request
from movies import Movies




app = FastAPI()

dataBase = [
    
]

       
# Path - filmes [GET]
@app.get("/filmes")
def get_movies():
    return dataBase

# Path - filmes [POST]
@app.post("/filmes")
def post_movies(movie : Movies):
    dataBase.append(movie)
    return movie

# Path - filmes/{id} 
@app.get("/filmes/{id}")
def getById(id : int):
    for movies in dataBase:
        if movies.id == id:
             return {"Name": movies.name}
    return {"ERROR": "Item not found"}