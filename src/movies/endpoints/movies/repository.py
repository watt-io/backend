from exception import RepositoryException, RepositoryNotFoundException
from movies.infrastructure.database.models.movies import Movies
from movies.infrastructure.repositories.repository import SqlRepository
from sqlalchemy import select


class MoviesRepository(SqlRepository):
    model = Movies

    async def check_if_movie_already_exists(self, params):
        async with self.session_factory() as session:
            result = await session.execute(select(self.model).filter_by(**params))
            result = result.scalars().first()
        if result:
            raise RepositoryException('Movie already exists')

    async def filter_by_if_movie_exists(self, params):
        async with self.session_factory() as session:
            result = await session.execute(select(self.model).filter_by(**params))
            result = result.scalars().first()
        if not result:
            raise RepositoryNotFoundException('Movie not found')
        return result
