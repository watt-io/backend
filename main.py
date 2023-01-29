import pandas as pd
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

# Base feita para inserir um filme
class Item(BaseModel):
    NOME: str
    ANO: Optional[int] = None
    DIRETOR: Optional[str] = None

# Base feita para editar um filme
class UpdateItem(BaseModel):
    NOME: Optional[str] = None
    ANO: Optional[int] = None
    DIRETOR: Optional[str] = None

# Inicia a API
app = FastAPI()

# Cria um dataframe referente ao banco filmes.json
frame = pd.read_json('filmes.json', orient='columns')

# Transforma o dataframe em um dicionário para facilitar o uso
dados = frame.to_dict()

# Cria um dataframe referente ao banco config.json
config = pd.read_json('config.json', orient='values')

# Recebe o ID a ser considerado
id_base = config["ID"].loc[0]

@app.get("/")
async def homepage():
    return {"Data": "Bem Vindo!"}

@app.get("/filmes")
async def get_film():
    return dados

@app.get("/filmes/{id}")
async def get_id_film(id: int = Path(None, description="ID do Filme")):
    for i in dados["NOME"]:
        if dados["NOME"][i] == frame["NOME"].loc[id]:
            return {"NOME": dados["NOME"][i], "ANO": dados["ANO"][i], "DIRETOR": dados["DIRETOR"][i]}
    return {"Erro": "ID nao encontrado"}

@app.post("/filmes")
async def postfilm(item: Item):
    global frame
    global dados
    global id_base
    aux = pd.DataFrame({"NOME": item.NOME, "ANO": item.ANO, "DIRETOR": item.DIRETOR}, index=[id_base])
    frame = pd.concat([frame, aux])
    frame.to_json('filmes.json', orient="columns")
    dados = frame.to_dict()
    id_base += 1
    config["ID"].loc[0] = id_base
    config.to_json('config.json')
    return item

@app.put("/filmes/{id}")
def update_film(id: int, item: UpdateItem):
    global frame
    global dados
    global id_base
    if id not in dados["NOME"]:
        return {"Erro": "Nao existe esse ID"}
    if(item.NOME != None):
        frame["NOME"].loc[id] = item.NOME
    if(item.ANO != None):
        frame["ANO"].loc[id] = item.ANO
    if(item.DIRETOR != None):
        frame["DIRETOR"].loc[id] = item.DIRETOR
    print(frame)
    frame.to_json('filmes.json', orient="columns")
    dados = frame.to_dict()
    return item

@app.delete("/filmes/{id}")
def delete_film(id: int):
    global frame
    global dados
    if id not in dados["NOME"]:
        return {"Erro": "Nao existe esse ID"}
    frame = frame.drop(id)
    dados = frame.to_dict()
    frame.to_json("filmes.json", orient='columns')
    return {"Aviso": "Deletado o ID: {}".format(id)}
