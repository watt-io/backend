from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import models

class Filmes(BaseModel):
    _id: int = 0
    Title: str
    Duration: str
    Link: str
    
    def set_id(self, id):
        return {
            '_id': id,
            'Title': self.Title,
            'Duration': self.Duration,
            'Link': self.Link
        }

class Generos(BaseModel):
    _id: int = 0
    Name: str

    def set_id(self, id):
        return {
            '_id': id,
            'Name': self.Name
        }

app = FastAPI()

@app.get("/filmes")
def getFilmes():
    f_data = models.filmes_collection.find().sort("Title", 1)
    g_data = models.generos_collection.find().sort("_id", 1)
    filmes = []
    generos = []
    for genero in g_data:
        generos.append(genero.get("Name"))
    for doc in f_data:
        f_gen = []
        for gen in doc.get("Genres"):
            f_gen.append(generos[int(gen)-1])
        filme = Filmes(Title=doc.get("Title"), Duration=doc.get("Duration"), Link=doc.get("Link"), Genres=f_gen)
        filmes.append(dict(filme))
    return JSONResponse(content={"Data": filmes}, status_code=200)

@app.post("/filmes")
def postFilmes(filme: Filmes, generos: list[str]):
    f_data = models.filmes_collection.find({"Title": filme.Title})
    for filme in f_data:
        return JSONResponse(content={"Data": "Filme já cadastrado"}, status_code=406)
    g_data = list(models.generos_collection.find().sort("_id", 1))
    c_data = list(models.control_collection.find({"Type": "Filme"}))[0].get("Number")
    size = len(g_data)
    g_array = []
    for genre in generos:
        for i in range(size):
            if genre == g_data[i].get("Name"):
                g_array.append(g_data[i].get("_id"))
                break
    if len(generos) == len(g_array):
        new_filme = dict(filme.set_id(c_data+1))
        relations = []
        for gen in g_array:
            relations.append({"Movie": c_data+1, "Genre": gen})
        models.filmes_collection.insert_one(new_filme)
        models.filmes_generos_collection.insert_many(relations)
        models.control_collection.find_one_and_update({"Type": "Filme"}, {"$set":{"Number": c_data+1}})
        return JSONResponse(content={"Data": "Filme " + filme.Title + " cadastrado com sucesso"}, status_code=201)
    else:
        return JSONResponse(content = {"Data": "Gêneros não cadastrados"}, status_code=404)

@app.get("/filmes/{id}")
def getFilme(id: int):
    data = models.filmes_collection.find_one({"_id": id}, {"_id":0})
    if not data:
        return JSONResponse(content={"Data": "Filme não encontrado"}, status_code=404)
    generos = []
    for gen in data.get("Genres"):
        g_data = models.generos_collection.find_one({"_id": int(gen)}, {"_id": 0})
        generos.append(g_data.get("Name"))
    filme = Filmes(Title=data.get("Title"), Duration=data.get("Duration"), Link=data.get("Link"), Genres=generos)
    return JSONResponse(content={"Data": dict(filme)}, status_code=200)

@app.delete("/filmes/{id}")
def deleteFilmes(id: int):
    f_data = models.filmes_collection.find_one_and_delete({"_id": id})
    if not f_data:
        return JSONResponse(content={"Data": "Filme não encontrado"}, status_code=404)
    models.filmes_generos_collection.delete_many({"Movie": id})
    return JSONResponse(content={"Data": "Filme " + f_data.get("Title") + " foi deletado"}, status_code=200)

@app.get("/generos")
def getGenero():
    g_data = models.generos_collection.find().sort("_id", 1)
    generos = []
    for genero in g_data:
        generos.append(genero.get("Name"))
    return JSONResponse(content={"Data": generos}, status_code=200)

@app.post("/generos")
def postGenero(genero: Generos):
    g_data = list(models.generos_collection.find({"Name": genero.Name}))
    for genero in g_data:
        return JSONResponse(content={"Data": "Genero já cadastrado"}, status_code=406)
    c_data = list(models.control_collection.find({"Type": "Genero"}))[0].get("Number")
    new_genero = dict(genero.set_id(c_data+1))
    models.generos_collection.insert_one(new_genero)
    models.control_collection.find_one_and_update({"Type": "Genero"}, {"$set":{"Number": c_data+1}})
    return JSONResponse(content={"Data": "Genero " + genero.Name + " cadastrado com sucesso"}, status_code=201)

@app.delete("/generos/{id}")
def deleteGenero(id: int):
    g_data = models.generos_collection.find_one({"_id": id})
    if not g_data:
        return JSONResponse(content={"Data": "Esse genero não existe no nosso banco de dados"}, status_code=404)
    models.filmes_generos_collection.delete_many({"Genre": id})
    genero_deletado = models.generos_collection.find_one_and_delete({"_id": id})
    return JSONResponse(content={"Data": "Genero " + genero_deletado.get("Name") + " deletado com sucesso"})