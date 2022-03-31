from fastapi import FastAPI
from pydantic import BaseModel
from movie_repository import Repository
from movie_model import Movie

app = FastAPI()
repository = Repository()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/filmes")
def save_item(id: str, name: str, year: int, cast: list, genre: str, director: str):
    repository.save_item(id, name, year, cast, genre, director)
    return repository.read_items()
    #Deve criar um filme novo

# Read ---------------------------------------------------------
@app.get("/filmes")
def read_items():
    return repository.read_items()
    #Deve retornar todos os filmes cadastrados

@app.get("/filmes/{id}")
def read_by_id(id : str):
    return repository.read_by_id(id)
    #Deve retornar um filme pelo id

# Update -------------------------------------------------------
@app.put("/filmes/{id}")
def update_by_id(id: str, key : str, value):
    repository.update_item(id, key, value)
    return repository.read_by_id(id)
    #Deve atualizar um filme pelo id

# Delete -------------------------------------------------------
@app.delete("/filmes/{id}")
def delete_by_id(id : str):
    repository.delete_item(id)
    return repository.read_items()
    #Deve deletar um filme pelo id
