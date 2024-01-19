import json
import pathlib
from fastapi import FastAPI, Response, Depends
from sqlmodel import Session, select
from typing import List,Union
from models import Filme
from database import FilmeModelo, engine

app = FastAPI()
data = []
@app.on_event("startup")
async def startup_event():
    DATAFILE = pathlib.Path() / 'data' / 'data.json'

    session = Session(engine)

    try:
        statement = select(FilmeModelo)
        result = session.exec(statement).first()

        if result is None:
            filmes = json.load(f)
            for filme_data in filmes:
                filme = FilmeModelo(**filme_data)
                session.add(filme)

        session.commit()

    except Exception as e:
        print(f"Erro durante a inicialização: {e}")

    finally:
        session.close()

def get_session():
    with Session(engine) as session:
        yield session

@app.get('/filmes/', response_model=List[Filme])
def filmes(session: Session= Depends(get_session)):
    statement = select(FilmeModelo)
    result = session.exec(statement).all()
    return result

@app.get('/filmes/{id_filme}', response_model=Union[Filme, str])
def filme(id_filme: int, response: Response, session: Session= Depends(get_session)):
    filme = session.get(FilmeModelo, id_filme)
    if filme is None:
        response.status_code = 404
        return "Filme não encontrado!"
    return filme

@app.post('/filmes/', response_model=Filme, status_code=201)
def create_filme(filme: FilmeModelo, session: Session = Depends(get_session)):
    session.add(filme)
    session.commit()
    session.refresh(filme)
    return filme

@app.put('/filmes/{filme_id}', response_model=Filme, status_code=201)
def update_filme(filme_id: int, updated_filme: Filme, response: Response, session: Session = Depends(get_session)):

    filme = session.get(FilmeModelo, filme_id)

    if filme is None:
        response.status_code = 204
        return "Filme não encontrado!"

    filme = session.get(FilmeModelo, filme_id)
    filme_dict = updated_filme.dict(exclude_unset=True)
    for key, val in filme_dict.items():
        setattr(filme, key, val)
    session.add(filme)
    session.commit()
    session.refresh(filme)
    return filme

@app.delete('/filmes/{filme_id}', response_model=Filme, status_code=201)
def update_filme(filme_id: int, response: Response, session: Session = Depends(get_session)):

    filme = session.get(FilmeModelo, filme_id)
    if filme is None:
        response.status_code = 204
        return "Filme não encontrado!"

    session.delete(filme)
    session.commit()
    return Response(status_code=200)
