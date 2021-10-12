from os import name
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

#Criar o modelo
class Filmes(BaseModel):
    id: int
    name: str
    gender: str
    year: int 

#Cria base de dados
data_base=[
    Filmes(id=1, name="Vingadores", gender="Action", year=2012),
    Filmes(id=2, name="Batman: O Cavaleiro das Trevas", gender="Action", year=2008),
    Filmes(id=3, name="Homem-Aranha: Sem volta pra casa", gender="Action", year=2021),
]

#Get de todos os filmes
@app.get("/filmes")
def get_all_movies():
    return data_base

#Get do filme por id
@app.get("/filmes/{id_movie}")
def get_movie_id(id_movie: int):
    for filme in data_base:
        if(filme.id == id_movie):
            return filme
    return {"Status": 404, "Mensagem": "Não foi possível localizar o filme"}

#Post do filme
@app.post("/filmes")
def post_movie(filme: Filmes):
    data_base.append(filme)
    return filme


#Deleta todos os filmes
@app.delete("/filmes")
def delete_all_movies():
    data_base.clear()
    return data_base


#Deleta filme por id
@app.delete("/filmes/{id_movie}")
def delete_movie_id(id_movie: int):
   for filme in data_base:
        if(filme.id == id_movie):
            data_base.pop(id_movie-1)
            return data_base
            

#Update do filme
@app.put("/filmes/{id_movie}")
def update_movie_id(id_movie: int, filme: Filmes):
    data_base[id_movie-1] = filme
    return data_base
