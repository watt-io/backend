import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from app.crud.filmes import CRUDMovie
from app.crud.usuarios import CRUDUser
from app.schemas.filme import MovieCreate, MovieUpdate
from app.schemas.usuario import UserCreate, UserUpdate
from app.models.filme import Movie
from app.models.usuario import User


class TestCRUDMovie:

    def test_create_movie(self, db_session):
        crud = CRUDMovie()
        movie_data = MovieCreate(
            title="Test Movie",
            year=2024,
            director="Test Director",
            genre="Action",
            synopsis="Test Synopsis",
            duration=120,
            rating=8.5,
        )

        movie = crud.create(db_session, movie_data)

        assert movie.title == movie_data.title
        assert movie.year == movie_data.year
        assert movie.id is not None

    def test_get_movie(self, db_session, mock_movie):
        crud = CRUDMovie()
        db_session.add(mock_movie)
        db_session.commit()

        movie = crud.get(db_session, mock_movie.id)

        assert movie is not None
        assert movie.id == mock_movie.id
        assert movie.title == mock_movie.title

    def test_get_movie_not_found(self, db_session):
        crud = CRUDMovie()

        movie = crud.get(db_session, 999)

        assert movie is None

    def test_get_all_movies(self, db_session):
        crud = CRUDMovie()

        movies = []
        for i in range(3):
            movie = Movie(
                title=f"Movie {i+1}",
                year=2020 + i,
                director=f"Director {i+1}",
                genre="Action",
                synopsis=f"Synopsis {i+1}",
                duration=120,
                rating=8.0,
            )
            movies.append(movie)
            db_session.add(movie)
        db_session.commit()

        result = crud.get_all(db_session)

        assert len(result) == 3
        assert all(isinstance(m, Movie) for m in result)

    def test_get_all_movies_pagination(self, db_session):
        crud = CRUDMovie()

        for i in range(5):
            movie = Movie(
                title=f"Movie {i+1}",
                year=2020 + i,
                director=f"Director {i+1}",
                genre="Action",
                synopsis=f"Synopsis {i+1}",
                duration=120,
                rating=8.0,
            )
            db_session.add(movie)
        db_session.commit()

        result = crud.get_all(db_session, limit=3)
        assert len(result) == 3

        result = crud.get_all(db_session, skip=2, limit=2)
        assert len(result) == 2
        assert result[0].title == "Movie 3"

    def test_update_movie(self, db_session, mock_movie):
        crud = CRUDMovie()
        db_session.add(mock_movie)
        db_session.commit()

        update_data = MovieUpdate(title="Updated Title", rating=9.0)

        movie = crud.update(db_session, mock_movie.id, update_data)

        assert movie is not None
        assert movie.title == "Updated Title"
        assert movie.rating == 9.0
        assert movie.year == mock_movie.year

    def test_update_movie_not_found(self, db_session):
        crud = CRUDMovie()
        update_data = MovieUpdate(title="New Title")

        movie = crud.update(db_session, 999, update_data)

        assert movie is None

    def test_delete_movie(self, db_session, mock_movie):
        crud = CRUDMovie()
        db_session.add(mock_movie)
        db_session.commit()

        success = crud.delete(db_session, mock_movie.id)

        assert success is True

        movie = crud.get(db_session, mock_movie.id)
        assert movie is None

    def test_delete_movie_not_found(self, db_session):
        crud = CRUDMovie()

        success = crud.delete(db_session, 999)

        assert success is False

    def test_get_by_title(self, db_session, mock_movie):
        crud = CRUDMovie()
        db_session.add(mock_movie)
        db_session.commit()

        movie = crud.get_by_title(db_session, mock_movie.title)

        assert movie is not None
        assert movie.title == mock_movie.title

    def test_get_by_genre(self, db_session):
        crud = CRUDMovie()

        movies = [
            Movie(title="Action 1", genre="Action", year=2020, director="Director 1"),
            Movie(title="Action 2", genre="Action", year=2021, director="Director 2"),
            Movie(title="Drama 1", genre="Drama", year=2022, director="Director 3"),
        ]
        for movie in movies:
            db_session.add(movie)
        db_session.commit()

        result = crud.get_by_genre(db_session, "Action")

        assert len(result) == 2
        assert all(m.genre == "Action" for m in result)


class TestCRUDUser:

    def test_create_user(self, db_session):

        crud = CRUDUser()
        user_data = UserCreate(
            email="test@example.com", password="123456", name="Test User"
        )

        user = crud.create(db_session, user_data)

        assert user.email == user_data.email
        assert user.name == user_data.name
        assert user.password_hash is not None
        assert user.password_hash != user_data.password

    def test_get_user(self, db_session, mock_user):
        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        user = crud.get(db_session, mock_user.id)

        assert user is not None
        assert user.id == mock_user.id
        assert user.email == mock_user.email

    def test_get_user_by_email(self, db_session, mock_user):
        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        user = crud.get_by_email(db_session, mock_user.email)

        assert user is not None
        assert user.email == mock_user.email

    def test_authenticate_success(self, db_session, mock_user):
        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        saved_user = crud.get_by_email(db_session, mock_user.email)
        assert saved_user is not None

        user = crud.authenticate(db_session, mock_user.email, "123456")

        assert user is not None
        assert user.email == mock_user.email

    def test_authenticate_wrong_password(self, db_session, mock_user):
        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        user = crud.authenticate(db_session, mock_user.email, "wrong_password")

        assert user is None

    def test_authenticate_user_not_found(self, db_session):
        crud = CRUDUser()

        user = crud.authenticate(db_session, "nonexistent@example.com", "123456")

        assert user is None

    def test_update_user(self, db_session, mock_user):
        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        update_data = UserUpdate(
            name="Updated Name", email="updated@example.com"
        )

        user = crud.update(db_session, mock_user.id, update_data)

        assert user is not None
        assert user.name == "Updated Name"
        assert user.email == "updated@example.com"

    def test_update_user_password(self, db_session, mock_user):
        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        update_data = UserUpdate(password="new_password_123")

        user = crud.update(db_session, mock_user.id, update_data)

        assert user is not None

        auth_user = crud.authenticate(
            db_session, mock_user.email, "new_password_123"
        )
        assert auth_user is not None

    def test_delete_user(self, db_session, mock_user):

        crud = CRUDUser()
        db_session.add(mock_user)
        db_session.commit()

        success = crud.delete(db_session, mock_user.id)

        assert success is True

        user = crud.get(db_session, mock_user.id)
        assert user is None
