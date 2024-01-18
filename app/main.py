from fastapi import FastAPI
from app.repositories.movie_repository import MovieRepository
from app.config import db_config
from app.models.movie import Movie, MovieData 

app = FastAPI()
movieRepository = MovieRepository(db_config)

@app.get("/")
def initial():
    return {"Hello": "World"}

@app.post("/filmes/", response_model=MovieData)
def createMovie(movie: Movie):
    return movieRepository.createMovie(movie)

@app.get("/filmes/", response_model=list[MovieData])
def getMovies():
    return movieRepository.getMovies()

@app.get("/filmes/{movie_id}", response_model=MovieData)
def getMovieById(movie_id: int):
    return movieRepository.getMovieById(movie_id)

@app.put("/filmes/", response_model=MovieData)
def updateMovie(updatedMovie: MovieData):
    return movieRepository.updateMovie(updatedMovie)

@app.delete("/filmes/{movie_id}", response_model=MovieData)
def deleteMovie(movie_id: int):
    return movieRepository.deleteMovie(movie_id)
