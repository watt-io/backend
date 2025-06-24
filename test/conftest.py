from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from testcontainers.postgres import PostgresContainer  # type: ignore

from movies.data.config.base import Base
from movies.run import app


@pytest.fixture(scope='session')
def engine() -> Generator[Engine, None, None]:
    with PostgresContainer('postgres:17-alpine', driver='psycopg') as pc:
        database_connection_string = pc.get_connection_url()

        with pytest.MonkeyPatch.context() as mp:
            mp.setenv('DATABASE_URL', database_connection_string)

            _engine = create_engine(database_connection_string)

            with _engine.begin():
                Base.metadata.create_all(_engine)
                yield _engine
                Base.metadata.drop_all(_engine)


@pytest.fixture
def client(engine: Engine) -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def movie_payload() -> dict[str, Any]:
    return {
        'title': 'The Matrix',
        'overview': 'A hacker learns the truth about reality and his role in the war against its controllers.',
        'year': 1999,
        'rating': 8.7,
        'category': 'Sci-Fi',
    }
