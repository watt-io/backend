from fastapi import FastAPI
from pydantic import BaseModel
import models

class Filmes(BaseModel):
    _id: int = 0
    Title: str
    Duration: str
    Link: str
    Genres: list[str]
    
    def set_id(self, id, g_id):
        return {
            '_id': id,
            'Title': self.Title,
            'Duration': self.Duration,
            'Link': self.Link,
            'Genres': g_id
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
    f_data = models.filmes_collection.find().sort("Title",)
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
        filmes.append(filme)
    return {"Data": filmes}

@app.post("/filmes")
def postFilmes(filme: Filmes):
    try:
        f_data = models.filmes_collection.find({"Title": filme.Title})
        for filme in f_data:
            return {"Data": "Filme já cadastrado"}
        g_data = list(models.generos_collection.find().sort("_id", 1))
        c_data = list(models.control_collection.find({"Type": "filme"}))[0].get("Number")
        size = len(g_data)
        g_array = []
        for genre in filme.Genres:
            for i in range(size):
                if genre == g_data[i].get("Name"):
                    g_array.append(str(g_data[i].get("_id")))
                    break
        if len(filme.Genres) == len(g_array):
            new_filme = dict(filme.set_id(c_data+1, g_array))
            models.filmes_collection.insert_one(new_filme)
            models.control_collection.find_one_and_update({"Type": "filme"}, {"$set":{"Number": c_data+1}})
            return {"Data": "Filme " + filme.Title + " cadastrado com sucesso"}
        else:
            return {"Data": "Generos não cadastrados"}
    except:
        return {"Data": "houve algum problema com o banco dados"}

@app.get("/filmes/{id}")
def getFilme(id: int):
    data = models.filmes_collection.find_one({"_id": id}, {"_id":0})
    generos = []
    for gen in data.get("Genres"):
        g_data = models.generos_collection.find_one({"_id": gen.get("G_id")}, {"_id": 0})
        generos.append(g_data.get("Name"))
    filme = Filmes(Title=data.get("Title"), Duration=data.get("Duration"), Link=data.get("Link"), Genres=generos)
    return {"Data": filme}

@app.get("/generos")
def getGenero():
    g_data = models.generos_collection.find().sort("_id", 1)
    generos = []
    for genero in g_data:
        generos.append(genero.get("Name"))
    return {"Data": generos}

@app.post("/generos")
def postGenero(genero: Generos):
    g_data = list(models.generos_collection.find({"Name": genero.Name}))
    for genero in g_data:
        return {"Data": "Genero já cadastrado"}
    c_data = list(models.control_collection.find({"Type": "genero"}))[0].get("Number")
    new_genero = dict(genero.set_id(c_data+1))
    models.generos_collection.insert_one(new_genero)
    models.control_collection.find_one_and_update({"Type": "genero"}, {"$set":{"Number": c_data+1}})
    return {"Data": "Genero " + genero.Name + " cadastrado com sucesso"}