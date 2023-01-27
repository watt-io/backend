from fastapi import FastAPI
from classes import Filmes
import models

app = FastAPI()

@app.get("/filmes")
def getFilmes():
    try:
        f_data = models.filmes_collection.find().sort("Title",)
        g_data = models.generos_collection.find().sort("_id", 1)
        filmes = []
        generos = []
        for gen in g_data:
            generos.append(gen.get("Name"))
        for doc in f_data:
            f_gen = []
            for gen in doc.get("Genres"):
                f_gen.append(generos[gen.get("G_id")-1])
            filme = Filmes(doc.get("Title"), doc.get("Duration"), doc.get("Link"), f_gen)
            filmes.append(filme)
        return {"Data": filmes}
    except:
        return {"Data": "Tivemos um erro inesperado"}

@app.put("/filmes")
def putFilmes():

    return {"Data": "On it"}

@app.get("/filmes/{id}")
def getFilme(id: int):
    try:
        data = models.filmes_collection.find_one({"_id": id}, {"_id":0})
        generos = []
        for gen in data.get("Genres"):
            g_data = models.generos_collection.find_one({"_id": gen.get("G_id")}, {"_id": 0})
            generos.append(g_data.get("Name"))
        filme = Filmes(data.get("Title"), data.get("Duration"), data.get("Link"), generos)
        print(generos)
        return {"Data": filme}
    except:
        return {"Data": "Tivemos um erro inesperado"}