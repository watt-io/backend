import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from jose import jwt
from app.auth.jwt_handler import (
    create_access_token,
    verify_token,
    get_password_hash,
    verify_password,
    SECRET_KEY,
    ALGORITHM,
)
from app.schemas.token import TokenData


class TestJWTHandler:

    def test_create_access_token(self):
        data = {"sub": "teste@exemplo.com"}

        token = create_access_token(data=data)

        assert token is not None
        assert isinstance(token, str)

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload["sub"] == data["sub"]

    def test_create_access_token_with_expires(self):
        data = {"sub": "teste@exemplo.com"}
        expires_delta = timedelta(minutes=60)

        token = create_access_token(data=data, expires_delta=expires_delta)

        assert token is not None

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload["sub"] == data["sub"]

        exp_timestamp = payload["exp"]
        exp_datetime = datetime.utcfromtimestamp(exp_timestamp)
        now = datetime.utcnow()

        time_diff = exp_datetime - now
        assert 59 <= time_diff.total_seconds() / 60 <= 61

    def test_verify_token_valid(self):
        data = {"sub": "teste@exemplo.com"}
        token = create_access_token(data=data)

        token_data = verify_token(token)

        assert token_data is not None
        assert isinstance(token_data, TokenData)
        assert token_data.email == data["sub"]

    def test_verify_token_invalid(self):
        token = "token_invalido"

        token_data = verify_token(token)

        assert token_data is None

    def test_verify_token_expired(self):
        data = {
            "sub": "teste@exemplo.com",
            "exp": datetime.utcnow() - timedelta(hours=1),
        }
        token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        token_data = verify_token(token)

        assert token_data is None

    def test_verify_token_wrong_secret(self):
        data = {"sub": "teste@exemplo.com"}
        token = jwt.encode(data, "wrong_secret", algorithm=ALGORITHM)

        token_data = verify_token(token)

        assert token_data is None

    def test_verify_token_no_subject(self):
        data = {"user_id": 123}
        token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        token_data = verify_token(token)

        assert token_data is None


class TestPasswordHandler:

    def test_get_password_hash(self):
        password = "minha_senha_123"

        hashed = get_password_hash(password)

        assert hashed is not None
        assert isinstance(hashed, str)
        assert hashed != password
        assert len(hashed) > len(password)

    def test_verify_password_correct(self):
        password = "minha_senha_123"
        hashed = get_password_hash(password)

        is_valid = verify_password(password, hashed)

        assert is_valid is True

    def test_verify_password_incorrect(self):
        password = "minha_senha_123"
        wrong_password = "senha_errada"
        hashed = get_password_hash(password)

        is_valid = verify_password(wrong_password, hashed)

        assert is_valid is False

    def test_verify_password_empty(self):
        password = ""
        hashed = get_password_hash(password)

        is_valid = verify_password(password, hashed)

        assert is_valid is True

    def test_password_hash_consistency(self):
        password = "minha_senha_123"

        hash1 = get_password_hash(password)
        hash2 = get_password_hash(password)

        assert hash1 != hash2
        assert verify_password(password, hash1) is True
        assert verify_password(password, hash2) is True


class TestTokenData:

    def test_token_data_creation(self):
        email = "teste@exemplo.com"

        token_data = TokenData(email=email)

        assert token_data.email == email

    def test_token_data_optional_email(self):
        token_data = TokenData(email=None)

        assert token_data.email is None
