from filmes.infrastructure.database.models.filmes import Movies
from filmes.infrastructure.repositories.repository import SqlRepository


class MoviesRepository(SqlRepository):
    model = Movies
