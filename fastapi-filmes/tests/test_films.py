import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

@pytest.mark.asyncio
async def test_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Filmes rodando!"}

@pytest.mark.asyncio
async def test_create_film():
    transport = ASGITransport(app=app)
    film_data = {
        "title": "Matrix",
        "director": "Wachowski",
        "year": 1999
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/filmes/", json=film_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == film_data["title"]
    assert "id" in data

@pytest.mark.asyncio
async def test_get_films():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/filmes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

