from fastapi.param_functions import Query
from src.db.repositories.base import BaseRepository
from src.models.filmes import FilmeCreate, FilmeInDB, FilmeBase

CREATE_FILME_QUERY = """
    INSERT INTO filmes (tittle)
    VALUES (:tittle)
    RETURNING id, tittle;
"""
ALL_FILME_QUERY = """
    SELECT * FROM public.filmes;	
"""
GET_BY_ID_FILME_QUERY = """
    SELECT *
    FROM public.filmes
    WHERE id = :id;
"""
class FilmeRepository(BaseRepository):
	async def create_filme(self, *, new_filme: FilmeCreate) -> FilmeInDB:
		query_values = new_filme.dict()
		filme= await self.db.fetch_one(query=CREATE_FILME_QUERY, values=query_values)
		return FilmeInDB(**filme)

	async def get_filme(self) -> FilmeBase:
		filme_query= await self.db.fetch_all(query=ALL_FILME_QUERY)
		if filme_query:
			return filme_query
		else:
			return ("CLEAN_TABLE")

	async def get_filme_by_id(self, *, id:int) -> FilmeInDB:
		filme_query = await self.db.fetch_one(query=GET_BY_ID_FILME_QUERY, values={"id":id})
		if filme_query:
			return FilmeInDB(**filme_query)
		else:
			return("FILME_NAO_ENCONTRADO")