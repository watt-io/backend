from typing import Dict, List

from exception import RepositoryException
from movies.endpoints.movies.repository import MoviesRepository
from movies.infrastructure.database.models.movies import Movies


class MoviesService:
    def __init__(self, movies_repository: MoviesRepository):
        self.movies_rep = movies_repository

    async def check_if_movie_already_exists(self, movie_name: str):
        movie = await self.movies_rep.filter_by({'name': movie_name})
        if movie:
            raise RepositoryException('Movie already exists')

    async def create_movie(self, movie_date: Dict):
        await self.check_if_movie_already_exists(movie_name=movie_date.get('name'))
        movie = await self.movies_rep.create(movie_date)
        return movie

    async def get_movie_by_id(self, movie_id: int) -> Movies:
        movie = await self.movies_rep.filter_by_if_movie_exists({'id': movie_id})
        return movie

