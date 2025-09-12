from fastapi import HTTPException
from sqlalchemy.orm import Session
from Repositories.FilmRepository import FilmRepository
from DTOs.FilmDTOs import FilmCreate

class FilmService:
    def __init__(self, db: Session):
        self.repo = FilmRepository(db)

    def create_film(self, film_data: FilmCreate):
        # Exemplo de regra de negócio: duração mínima
        if film_data.duration <= 0:
            raise ValueError("A duração do filme deve ser maior que zero.")
        return self.repo.create(film_data)

    def list_films(
        self,
        page: int = 1,
        page_size: int = 10,
        title: str | None = None,
        category: str | None = None,
        language: str | None = None,
        release_year: int | None = None,
    ):
        if page < 1: page = 1
        if page_size < 1: page_size = 10

        skip = (page - 1) * page_size
        return self.repo.list_all(
            skip=skip,
            limit=page_size,
            title=title,
            category=category,
            language=language,
            release_year=release_year
        )

    def get_film(self, film_id: int):
        book = self.repo.get_by_id(book_id)
        if not book:
            raise ValueError("Filme não encontrado.")
        return film

    def update_film(self, film_id: int, film_data: FilmCreate):
        film = self.repo.update(film_id, film_data)
        if not film:
            raise HTTPException(status_code=404, detail="Filme não encontrado.")
        return film

    def delete_film(self, film_id: int):
        film = self.repo.delete(film_id)
        if not film:
            raise HTTPException(status_code=404, detail="Filme não encontrado")
        return film
