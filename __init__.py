from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


from views.serializer.to_json import build_toJson
from views.default_schemas import Schemas
from views.movie_schemas import Movie
from models.orm import orm_movies

from models.db_conn.sqlite import get_db, metadata, engine

api = FastAPI()
metadata.create_all(bind=engine)

@api.get("/", response_model=Schemas)
async def home():
    msg = "Api connection successfully"
    return build_toJson(200,msg)

@api.post("/v1/api/movies")
async def post_movies(movie: Movie, db: Session = Depends(get_db)):
    movie = orm_movies.add_movies(db, movie)
    if (movie):
        msg = "User created successfully"
        return build_toJson(status=200, content=movie, alert=msg)
    else:
        msg = "User not created"
    return build_toJson(status=401, content=None, alert=msg)   



@api.get("/v1/api/movies", response_model=Schemas)
async def get_all_movies(skip: int =0, limit: int = 10, db: Session =  Depends(get_db)):
    query = orm_movies.get_movies(db, skip=skip, limit=limit)
    if (query):
        msg = "Return all movies here"
        return build_toJson(200, content=query ,alert=msg)
    else:
        msg = "Not found movies"
        return build_toJson(200, msg)

