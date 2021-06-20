from src.db.repositories.base import BaseRepository
from src.models.filmes import FilmeCreate, FilmeInDB

CREATE_FILMES_QUERY = """
    INSERT INTO filmes (tittle
    VALUES (:tittle)
    RETURNING id, tittle;
"""

class FilmeRepository(BaseRepository):
	async def create_filme(self, *, new_filme: FilmeCreate) -> FilmeInDB:
		query_value = new_cleaning.dict()
		filme= await self.db.fetch_one(query=CREATE_FILME_QUERY, values=query_values)

		return FilmeInDB(**cleaning)