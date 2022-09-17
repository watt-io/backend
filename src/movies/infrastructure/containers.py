from dependency_injector import containers, providers

from config import Config


from filmes.endpoints.filmes.repository import MoviesRepository
from filmes.endpoints.filmes.service import MoviesService
from filmes.infrastructure.database.database_sql import PostgresDatabase


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    postgres_db = providers.Singleton(PostgresDatabase, database_url=Config.DATABASE_URL)

    # repository
    movies_repository = providers.Factory(MoviesRepository, session_factory=postgres_db.provided.session)

    # services
    users_services = providers.Factory(MoviesService, movies_repository=movies_repository,)
