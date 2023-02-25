from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Filme
from database import engine, Base, get_db
from repositories import FilmesRepository
from schemas import FilmesRequest, FilmesResponse
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cria um filme no banco de dados usando o método POST e retorna o filme criado

@app.post("/filmes", response_model=FilmesResponse, status_code=status.HTTP_201_CREATED)
def create_filme(request: FilmesRequest, db: Session = Depends(get_db)):
    filme = FilmesRepository.create(db, Filme(**request.dict()))
    return FilmesResponse.from_orm(filme)

# Lista todos os filmes do banco de dados usando o método GET

@app.get("/filmes", response_model=list[FilmesResponse])
def get_filmes(db: Session = Depends(get_db)):
    filmes = FilmesRepository.get_all(db)
    return [FilmesResponse.from_orm(filme) for filme in filmes]

#Lista um filme específico do banco de dados usando o método GET passando o id do filme como parâmetro

@app.get("/filmes/{id}", response_model=FilmesResponse)
def get_filme(id: int, db: Session = Depends(get_db)):
    filme = FilmesRepository.find_by_id(db, id)
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
    return FilmesResponse.from_orm(filme)

# Delete um filme do banco de dados usando o método DELETE passando o id do filme como parâmetro

@app.delete("/filmes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_filme(id: int, db: Session = Depends(get_db)):
    filme = FilmesRepository.find_by_id(db, id)
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
    FilmesRepository.delete(db, id)
    return FilmesResponse.from_orm(filme)

# Atualiza um filme do banco de dados usando o método PUT passando o id do filme como parâmetro

@app.put("/filmes/{id}", response_model=FilmesResponse)
def update_filme(id: int, request: FilmesRequest, db: Session = Depends(get_db)):
    if not FilmesRepository.find_by_id(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
    filme = FilmesRepository.update(db, Filme(id=id , **request.dict()))
    return FilmesResponse.from_orm(filme)
