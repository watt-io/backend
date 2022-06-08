
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import sqlite3


class filme(BaseModel):
    cod: int
    titulo: str
    ano: str
    genero: str
    descricao: str
    avaliacao: str
    
#Confirma a Base de dados
conn = sqlite3.connect("desafio.db", check_same_thread=False)
cnx = conn.cursor()
cnx.execute("CREATE TABLE IF NOT EXISTS FILMES(filme_cod integer unique, info json)")


app = FastAPI()
#Retorna todos os filmes no banco de dados
@app.get("/filmes")
def getFilme():
    resultado = cnx.execute("""SELECT * FROM FILMES""")
    return resultado.fetchall()

#Cadastrar novo Filme
@app.post("/filmes")
def postFilme(filme: filme):
    valores = {"titulo": filme.titulo, "ano": filme.ano, "genero": filme.genero, "descricao": filme.descricao, "avaliacao": filme.avaliacao}
    cnx.execute(f"""INSERT INTO FILMES (filme_cod, info) Values( {filme.cod} , "{valores}" );""")
    conn.commit()
    return "Filme: "+ str(filme.cod) + " - "+  filme.titulo + " adicionado ao Catalogo."
    

#Retorna o filme com ID específico
@app.get("/filmes/{id}")
def getFilmeID(id: int):
    resultado = cnx.execute(f"""SELECT * FROM FILMES WHERE FILME_COD = {id}""")
    return resultado.fetchall()[0]