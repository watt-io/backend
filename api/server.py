import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel

conexao = mysql.connector.connect(
    host = 'db-mysql',
    user = 'root',
    password = '1234',
    database = 'TesteBackend',
    port = '3306'
)

cursor = conexao.cursor()

class Filme(BaseModel):
    titulo: str

app = FastAPI()


@app.get("/filmes")
async def root():
    cursor.execute('SELECT nomeFilme FROM TesteBackend.Filmes')
    consulta = cursor.fetchall()
    filmes = [{"titulo": filme[0]} for filme in consulta]
    return {"Filmes": filmes}


@app.post("/filmes")
async def addFilme(filme: Filme):
    cursor.execute(f'INSERT INTO Filmes (nomeFilme) VALUES ("{filme.titulo}")')
    conexao.commit()
    return {"Message": "Filme cadastrado com sucesso"}


@app.get("/filmes/{id}")
async def searchFilme(id):
    try:
        int(id)
        cursor.execute(f'SELECT NomeFilme FROM TesteBackend.Filmes where idFilme={int(id)}')
        consulta = cursor.fetchall()
        filmes = [{"titulo": filme[0]} for filme in consulta]

        if(len(filmes)==0):
            return {"Message": "Não existe filme cadastrado com o id informado"}
        else:
            return {"Filme": filmes}
    except:
        return {"Message": "Id inválido"}