from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo
class Filme(BaseModel):
    id: int
    nome: str
    ano: int
    categoria: str

#Base de dados provisória
base_dados = [
    Filme(id=1, nome="Ex_Machina: Instinto artificial", ano=2014, categoria="Ficção científica"),
    Filme(id=2, nome="Matrix", ano=1999, categoria="Ficção científica"),
    Filme(id=3, nome="Piratas da informática", ano=1999, categoria="Drama/Docudrama")
]

@app.get('/filmes')
async def get_all_movies():
    return base_dados

@app.post('/filmes')
async def create_movie(filme: Filme):
    # editar as regras mais pra frente
    base_dados.append(filme)
    return filme

@app.get('/filmes/{id}')
async def get_a_movie(id: int):
    for filme in base_dados:
        if(filme.id == id):
            return filme
    
    return {"Status":404, "Message":"Movie not found"}