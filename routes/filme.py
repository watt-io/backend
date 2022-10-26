from fastapi import APIRouter
from config.db import conn
from model.index import filmes
from schemas.index import Filme

filme = APIRouter()

@filme.get("/filmes")
async def read_data():
    return conn.execute(filmes.select()).fetchall()

@filme.get("/filmes/{id}")
async def read_data(id: int):
    return conn.execute(filmes.select().where(filmes.c.id == id)).fetchall()

@filme.post("/filmes")
async def write_data(filme: Filme):
    conn.execute(filmes.insert().values(
        nome=filme.nome,
        genero=filme.genero,
        diretor=filme.diretor
    ))
    return conn.execute(filmes.select()).fetchall()

@filme.put("/filmes/{id}")
async def update_data(id:int,filme:Filme):
    conn.execute(filmes.update(
        nome=filme.nome,
        genero=filme.genero,
        diretor=filme.diretor
    ).where(filmes.c.id == id))
    return conn.execute(filmes.select()).fetchall()

@filme.delete("/")
async def delete_data():
    conn.execute(filmes.delete().where(filmes.c.id == id))
    return conn.execute(filmes.select()).fetchall()