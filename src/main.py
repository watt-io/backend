from typing import TYPE_CHECKING, List
import sqlalchemy.orm as _orm
import fastapi as _fastapi
import src.schemas as _schemas
import src.services as _services


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

_services._add_tables()

app = _fastapi.FastAPI()


@app.get("/movies", response_model=List[_schemas.Movie])
async def get_movies(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_movies(db)


@app.get("/movies/{id}", response_model=_schemas.Movie)
async def get_movie(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):

    movie = await _services.get_movie(id, db)
    if movie is None:
        raise _fastapi.HTTPException(404, "Movie does not exists")

    return movie


@app.post("/movies", response_model=_schemas.Movie)
async def create_movie(
    movie: _schemas.CreateMovie,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_movie(movie, db)
