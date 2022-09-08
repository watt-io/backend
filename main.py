from email import message
from fastapi import FastAPI, Depends, HTTPException, status, Response, UploadFile, File
from sqlalchemy.orm import Session

from models import Filme
from db import engine, Base, get_db
from repo import FilmeRepository
from schema import FilmeRequest, FilmeResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


import pandas as pd
filmes = pd.read_csv('amazon_prime_titles.csv', header=None, index_col=0, squeeze=True)

@app.post("/api/upload", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def uploadCSV(db: Session = Depends(get_db)):
    for filme in filmes.values:
        filme_up = {
            "type": filme[0],
            "title": filme[1],
            "director": filme[2],
            "description": filme[10]	
        }
        if filme_up['type'] != 'Movie':
            continue
        filme = FilmeRepository.create(db, Filme(**filme_up))
    return FilmeResponse.from_orm(filme)
        
    

# requisição POST para criação de um novo filme
@app.post("/api/filmes", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def create(request: FilmeRequest, db: Session = Depends(get_db)):
    filme = FilmeRepository.create(db, Filme(**request.dict()))
    return FilmeResponse.from_orm(filme)

# requisição GET para listar todos os filmes
@app.get("/api/filmes", response_model=list[FilmeResponse])
def findAll(db: Session = Depends(get_db)):
    filmes = FilmeRepository.findAll(db)
    return [FilmeResponse.from_orm(filme) for filme in filmes]

# requisição GET para buscar um filme pelo id
@app.get("/api/filmes/{id}", response_model=FilmeResponse)
def findById(id: int, db: Session = Depends(get_db)):
    filme = FilmeRepository.findById(db, id)
    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    return FilmeResponse.from_orm(filme)

# requisição DELETE para deletar um filme pelo id
@app.delete("/api/filmes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    try:
        FilmeRepository.delete(db, id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    