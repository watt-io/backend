import sqlite3
from typing import Any, Dict, List

from fastapi import HTTPException

from src.main.repositories.movies_repository import (
    create_movie_repo,
    get_movie_by_id_repo,
    list_movies_repo,
)
from src.main.validators import MovieCreateValidator


def create_movie_service(body: MovieCreateValidator) -> Dict[str, Any]:
    data = body.model_dump()
    try:
        return create_movie_repo(data)
    except sqlite3.Error as exc:
        raise HTTPException(status_code=500, detail="Error saving movie") from exc


def list_movies_service() -> List[Dict[str, Any]]:
    try:
        return list_movies_repo()
    except sqlite3.Error as exc:
        raise HTTPException(status_code=500, detail="Error fetching movies") from exc


def get_movie_by_id_service(movie_id: int) -> Dict[str, Any]:
    try:
        movie = get_movie_by_id_repo(movie_id)
    except sqlite3.Error as exc:
        raise HTTPException(status_code=500, detail="Error fetching movie") from exc

    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie
