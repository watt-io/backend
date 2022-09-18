from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


from views.serializer.to_json import build_toJson
from views.default_schemas import DefaultSchemas
from views.movie_schemas import Movie
from models.orm import orm_movies

from models.db_conn.sqlite import get_db, metadata, engine

api = FastAPI()
metadata.create_all(bind=engine)

@api.get("/v1/api/home/", response_model=DefaultSchemas)
async def home():
    msg = "Api connection successfully"
    return build_toJson(200,msg)

@api.post("/v1/api/movies/")
async def post_movies(movie: Movie, db: Session = Depends(get_db)):
    movie = orm_movies.add_movies(db, movie)
    if (movie):
        msg = "Movie created successfully"
        return build_toJson(status=200, content=movie, alert=msg)
    else:
        msg = "Movie not created"
    return build_toJson(status=400, content=None, alert=msg)   

@api.get("/v1/api/movies/", response_model=DefaultSchemas)
async def get_all_movies(skip: int =0, limit: int = 10, db: Session =  Depends(get_db)):
    query = orm_movies.get_movies(db, skip=skip, limit=limit)
    if (query):
        msg = "Return all movies here"
        return build_toJson(200, content=query ,alert=msg)
    else:
        msg = "Not found movies"
        return build_toJson(400, msg)

@api.get("/v1/api/movies/{id_movie}", response_model=Movie)
async def get_by_id(id_movie: str, db: Session = Depends(get_db)):
    query = orm_movies.getbyid_movies(db, id_movie)
    if (query):
        msg = "Return user by id"
        return build_toJson(200, query, msg)
    else: 
        msg = "Movie not found"
        return build_toJson(400, alert=msg)

@api.put("/v1/api/movies/{id_movie}", response_model=Movie) 
async def put_by_id(id_movie: str, movie: Movie , db: Session = Depends(get_db)):
    update = orm_movies.update(db, id_movie, movie)
    return build_toJson(200, update)


@api.delete("/v1/api/movies/{id_movie}", response_model=Movie)
async def delete_by_id(id_movie: str, db: Session = Depends(get_db)):
    delete = orm_movies.delete(db, id_movie)
    return build_toJson(200, delete)