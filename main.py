from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from dto.Movie import Movie

WattIoBackendChallengeApi = FastAPI()

database: List[Movie] = [
    Movie(
        id=uuid4(),
        name="Harry Potter and the Sorcerer's Stone",
        year=2001,
        director="Chris Columbus",
        genre=["Adventure", "Family", "Fantasy"],
        imdb=7.6,
    ),
    Movie(
        id=uuid4(),
        name="Harry Potter and the Chamber of Secrets",
        year=2002,
        director="Chris Columbus",
        genre=["Adventure", "Family", "Fantasy"],
        imdb=7.5,
    ),
    Movie(
        id=uuid4(),
        name="Harry Potter and the Prisoner of Azkaban",
        year=2004,
        director="Alfonso Cuarón",
        genre=["Adventure", "Family", "Fantasy"],
        imdb=7.9,
    )
]


@ WattIoBackendChallengeApi.get("/filmes")
async def getAllMovies():
    return database


@ WattIoBackendChallengeApi.get("/filmes/{movie_id}")
async def getMovieById(movie_id: UUID):
    for movie in database:
        if(movie.id == movie_id):
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@ WattIoBackendChallengeApi.post("/filmes")
async def postMovie(movie: Movie):
    database.append(movie)
    return {"id": movie.id}
