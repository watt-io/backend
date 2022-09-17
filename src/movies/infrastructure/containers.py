from dependency_injector import containers, providers

from config import Config


from movies.endpoints.movies.repository import MoviesRepository
from movies.endpoints.movies.service import MoviesService
from movies.infrastructure.database.database_sql import PostgresDatabase


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    postgres_db = providers.Singleton(PostgresDatabase, database_url=Config.DATABASE_URL)

    # repository
    movies_repository = providers.Factory(MoviesRepository, session_factory=postgres_db.provided.session)

    # services
    movies_services = providers.Factory(MoviesService, movies_repository=movies_repository)
