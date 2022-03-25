from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


@app.post("/filmes/", response_model=_schemas.Filme)
def create_filme(
        filme: _schemas.FilmeCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_filme = _services.get_by_nome(db=db, nome=filme.nome)
    if db_filme:
        raise _fastapi.HTTPException(
            status_code=400, detail="Esse filme já foi cadastrado"
        )
    return _services.create_filme(db=db, filme=filme)


@app.get("/filmes/", response_model=List[_schemas.Filme])
def read_filmes(
        skip: int = 0,
        limit: int = 10,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
        filmes = _services.get_filmes(db=db, skip=skip, limit=limit)
        return filmes


@app.get("/filmes/{filme_id}", response_model=_schemas.Filme)
def read_filme(filme_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_filme = _services.get_filme(db=db, filme_id=filme_id)
    if db_filme is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="ID não cadastrado"
        )
    return db_filme
