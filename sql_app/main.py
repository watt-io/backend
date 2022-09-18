from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .models import Movie
from .database import engine, Base, get_db
from .crud import MovieRepository
from .schemas import MovieRequest, MovieResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()

#Adiciona um filme ao BD, se o titulo for diferente
@app.post("/filmes", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create(request: MovieRequest, db: Session = Depends(get_db)):
    
    movie = MovieRepository.find_by_title(db, Movie(**request.dict()))# Verifica se o filme ja existe
    if not movie:
        movie = MovieRepository.save(db, Movie(**request.dict()))#Se o filme nao existir eh criado
        return MovieResponse.from_orm(movie)
    else:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Filme ja existente"
        )
    
#Retornar uma lista com todos os filmes
@app.get("/filmes", response_model=list[MovieResponse])
def find_all(db: Session = Depends(get_db)):
    movies = MovieRepository.find_all(db)
    return [MovieResponse.from_orm(movie) for movie in movies]

#Retorna um filme pelo id (caso houver)
@app.get("/filmes/{id}", response_model=MovieResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    movie = MovieRepository.find_by_id(db, id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    return MovieResponse.from_orm(movie)


