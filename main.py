from fastapi import FastAPI, Depends, HTTPException, status, Response, UploadFile, File
from sqlalchemy.orm import Session
import pandas as pd
from fastapi_csv import FastAPI_CSV

from models import Filme
from db import engine, Base, get_db
from repo import FilmeRepository
from schema import FilmeRequest, FilmeResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()



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
def deletById(id: int, db: Session = Depends(get_db)):
    try:
        FilmeRepository.delete(db, id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)