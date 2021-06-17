from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_filmes() -> List[dict]:
	filmes = [
		{"id": 1, "tittle":"A VERY PYTHONIC MOVIE","cleaning_type":"full_clean" },
		{"id": 2, "tittle":"Bee Movie","cleaning_type":"full_clean" }
	]
	return filmes