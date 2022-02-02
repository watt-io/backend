from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas
from starlette.responses import RedirectResponse

app = _fastapi.FastAPI()

_services.create_database()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/filmes", response_model=List[_schemas.Movie])
async def show_movies(
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.get_movies(db)
     

@app.get("/filmes/{id}", response_model=_schemas.Movie)
async def show_movie(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    movie = await _services.get_movie(db, id)
    if movie is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this movie does not exist"
        )
    return movie

@app.post("/filmes", response_model=_schemas.Movie)
async def post_movie(movie: _schemas.MovieCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.put_movie(db, movie)
