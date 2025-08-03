import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from unittest.mock import Mock

from app.main import app
from app.database.connection import get_db, Base
from app.models.filme import Movie
from app.models.usuario import User
from app.schemas.filme import MovieCreate
from app.schemas.usuario import UserCreate
from app.auth.jwt_handler import create_access_token


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():

    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    app.dependency_overrides[get_db] = lambda: db_session
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def mock_user():
    from app.auth.jwt_handler import get_password_hash

    return User(
        id=1,
        email="test@example.com",
        password_hash=get_password_hash("123456"),
        name="Test User",
        created_at=datetime(2024, 1, 15, 10, 0, 0),
        updated_at=None,
    )


@pytest.fixture
def mock_movie():
    return Movie(
        id=1,
        title="Interstellar",
        year=2014,
        director="Christopher Nolan",
        genre="Science Fiction",
        synopsis="An astronaut travels through a wormhole",
        duration=169,
        rating=8.6,
        created_at=datetime(2024, 1, 15, 10, 0, 0),
        updated_at=None,
    )


@pytest.fixture
def token_jwt(mock_user):
    return create_access_token(data={"sub": mock_user.email})


@pytest.fixture
def headers_auth(mock_usuario):
    token = create_access_token(data={"sub": mock_usuario.email})
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def user_create_data():
    return {"email": "new@example.com", "password": "123456", "name": "New User"}


@pytest.fixture
def mock_usuario():
    from app.auth.jwt_handler import get_password_hash

    return User(
        id=1,
        email="test@example.com",
        password_hash=get_password_hash("123456"),
        name="Test User",
        created_at=datetime(2024, 1, 15, 10, 0, 0),
        updated_at=None,
    )


@pytest.fixture
def usuario_create_data():
    return {"email": "new@example.com", "password": "123456", "name": "New User"}


@pytest.fixture
def movie_create_data():
    return {
        "title": "The Godfather",
        "year": 1972,
        "director": "Francis Ford Coppola",
        "genre": "Drama",
        "synopsis": "The story of the Corleone family",
        "duration": 175,
        "rating": 9.2,
    }
