from fastapi import HTTPException
from sqlalchemy.orm import Session
from Repositories.DirectorRepository import DirectorRepository
from DTOs.DirectorDTOs import DirectorCreate

class DirectorService:
    def __init__(self, db: Session):
        self.repo = DirectorRepository(db)

    def create_director(self, director_data: DirectorCreate):
        return self.repo.create(director_data)

    def list_directors(self, page: int = 1, page_size: int = 10, name: str | None = None):
        if page < 1: page = 1
        if page_size < 1: page_size = 10
        skip = (page - 1) * page_size
        directors = self.repo.list_all(skip=skip, limit=page_size, name=name)
        if not directors:
            raise HTTPException(status_code=404, detail="Diretor não encontrado.")
        return directors

    def get_director(self, director_id: int):
        director = self.repo.get_by_id(director_id)
        if not director:
            raise HTTPException(status_code=404, detail="Diretor não encontrado.")
        return director

    def update_director(self, director_id: int, director_data: DirectorCreate):
        director = self.repo.update(director_id, director_data)
        if not director:
            raise HTTPException(status_code=404, detail="Diretor não encontrado.")
        return director

    def delete_director(self, director_id: int):
        director = self.repo.delete(director_id)
        if not director:
            raise HTTPException(status_code=404, detail="Diretor não encontrado")
        return director
