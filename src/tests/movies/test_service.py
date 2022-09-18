from unittest.mock import MagicMock

import factory
import pytest

from exception import RepositoryException
from movies.endpoints.movies.repository import MoviesRepository
from movies.endpoints.movies.service import MoviesService
from movies.infrastructure.database.models.movies import Movies


class MoviesFactory(factory.Factory):
    class Meta:
        model = Movies

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('name')
    description = factory.Faker('text')
    release_year = factory.Faker('year')
    created_at = factory.Faker('date_time')
    updated_at = factory.Faker('date_time')


@pytest.fixture
def sql_repository_movie_mock():
    sql_repository_movie_mock = MagicMock(spec=MoviesRepository)
    yield sql_repository_movie_mock


@pytest.fixture
def movie_service_mock(sql_repository_movie_mock):
    return MoviesService(movies_repository=sql_repository_movie_mock)


@pytest.fixture
def payload_create_movie():
    return {
        "name": "Star Wars 2",
        "description": "ci fi",
        "release_year": "1998"
    }


@pytest.mark.asyncio
async def test_check_if_movie_already_exists(movie_service_mock):
    movie_service_mock.movies_rep.filter_by.return_value = None
    response = await movie_service_mock.check_if_movie_already_exists(movie_name='test')
    assert response is None


@pytest.mark.asyncio
async def test_check_if_movie_already_exists_raise_exception(payload_create_movie, movie_service_mock):
    movie_service_mock.movies_rep.filter_by.return_value = MoviesFactory()
    with pytest.raises(RepositoryException):
        await movie_service_mock.check_if_movie_already_exists(movie_name=payload_create_movie)


@pytest.mark.asyncio
async def test_create_movie(app, movie_service_mock, sql_repository_movie_mock, payload_create_movie):
    movie_service_mock.movies_rep.filter_by.return_value = None
    movie_factory = MoviesFactory()
    sql_repository_movie_mock.create.return_value = movie_factory

    with app.container.movies_repository.override(sql_repository_movie_mock):
        response = await movie_service_mock.create_movie(movie_date=payload_create_movie)
        assert response.name == movie_factory.name
        assert response.description == movie_factory.description
        assert response.release_year == movie_factory.release_year
        assert response.release_year == movie_factory.release_year
        assert response.created_at == movie_factory.created_at
        assert response.updated_at == movie_factory.updated_at


@pytest.mark.asyncio
async def test_create_movie_already_exists(app, movie_service_mock, sql_repository_mock, payload_create_movie):
    movie_service_mock.movies_rep.filter_by.return_value = MoviesFactory()
    with pytest.raises(RepositoryException):
        await movie_service_mock.check_if_movie_already_exists(movie_name=payload_create_movie)


@pytest.mark.asyncio
async def test_get_movie_by_id(app, movie_service_mock, sql_repository_mock):
    movie_factory = MoviesFactory()
    movie_service_mock.movies_rep.filter_by_if_movie_exists.return_value = movie_factory

    response = await movie_service_mock.get_movie_by_id(movie_id=1)
    assert response.name == movie_factory.name
    assert response.description == movie_factory.description
    assert response.release_year == movie_factory.release_year
    assert response.release_year == movie_factory.release_year
    assert response.created_at == movie_factory.created_at
    assert response.updated_at == movie_factory.updated_at


@pytest.mark.asyncio
async def test_get_all_movies(app, movie_service_mock, sql_repository_mock):
    movie_factory = [MoviesFactory()]
    movie_service_mock.movies_rep.get_all.return_value = movie_factory

    response = await movie_service_mock.get_all_movies()
    assert response[0].name == movie_factory[0].name
    assert response[0].description == movie_factory[0].description
    assert response[0].release_year == movie_factory[0].release_year
    assert response[0].created_at == movie_factory[0].created_at
    assert response[0].updated_at == movie_factory[0].updated_at


@pytest.mark.asyncio
async def test_update_movie(app, movie_service_mock, sql_repository_mock):
    movie_factory = MoviesFactory()
    movie_service_mock.movies_rep.filter_by_if_movie_exists.return_value = movie_factory
    movie_service_mock.movies_rep.update.return_value = None

    response = await movie_service_mock.update_movie(movie_id=1, movie_data={'name': 'Indiana Jones'})
    assert response is None


@pytest.mark.asyncio
async def test_delete_movie(app, movie_service_mock, sql_repository_mock):
    movie_factory = MoviesFactory()
    movie_service_mock.movies_rep.filter_by_if_movie_exists.return_value = movie_factory
    movie_service_mock.movies_rep.delete.return_value = None

    response = await movie_service_mock.delete_movie(movie_id=1)
    assert response is None
