import asyncio
from unittest import mock

import pytest
from httpx import AsyncClient
from movies.infrastructure.database.database_sql import PostgresDatabase
from movies.infrastructure.repositories.repository import SqlRepository


@pytest.fixture
def db():
    PostgresDatabase.create_database = mock.MagicMock()


@pytest.fixture
def app(db):
    from app import create_app
    app = create_app()
    yield app


@pytest.fixture
def client(event_loop, app):
    client = AsyncClient(app=app, base_url='http://test')
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest.fixture
def sql_repository_mock():
    sql_repository_mock = mock.MagicMock(spec=SqlRepository)
    yield sql_repository_mock


def async_return(result):
    f = asyncio.Future()
    f.set_result(result)
    return f
