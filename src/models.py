from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://LucasOliveira:8GNEticXJDrGMBcR@cluster0.kwor4wz.mongodb.net/?retryWrites=true&w=majority")
    db = client.Backend
    print("Bd conectado")
except:
    print("A conexão com o bd falhou")

filmes_collection = db.Filmes
generos_collection = db.Generos
control_collection = db.Control
filmes_generos_collection = db.FilmesGeneros

filmes_schema = {
    "Title": {"type": "string", "required": "true"},
    "Duration": {"type": "string", "required": "true"},
    "Link": {"type": "string", "required": "true"}
}

filmes_generos_schema ={
    "Movie": {"yype": "int32", "required": "true"},
    "Genre": {"yype": "int32", "required": "true"}
}

generos_schema = {
    "Name": {"type": "string", "required": "true"}
}

control_schema = {
    "Type": {"type": "string", "required": "true"},
    "Number": {"type": "int32", "required": "true"}
}