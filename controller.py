from typing import Optional
from fastapi import FastAPI
import movie_repository as repository
import Movie

app = FastAPI()

# Create -------------------------------------------------------
@app.put("/filmes")
def save_item(movie):
    repository.save_item(movie)
    #Deve criar um filme novo

# Read ---------------------------------------------------------
@app.get("/filmes")
def read_items():
    repository.read_items()
    #Deve retornar todos os filmes cadastrados

@app.get("/filmes/{id}")
def read_by_id(id : int):
    repository.read_by_id(id)
    #Deve retornar um filme pelo id

# Update -------------------------------------------------------
@app.put("/filmes/{id}")
def update_by_id(id : int, movie : Movie):
    repository.update_item(id, movie)
    #Deve atualizar um filme pelo id

# Delete -------------------------------------------------------
@app.delete("/filmes/{id}")
def delete_by_id(id : int):
    repository.delete_item(id)
    #Deve deletar um filme pelo id
