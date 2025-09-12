from fastapi import HTTPException
from sqlalchemy.orm import Session
from Repositories.FilmRepository import FilmRepository
from DTOs.FilmDTOs import FilmCreate
from Repositories.CategoryRepository import CategoryRepository
from Repositories.DirectorRepository import DirectorRepository
class FilmService:
    def __init__(self, db: Session):
        self.repofilm = FilmRepository(db)
        self.repocatory = CategoryRepository(db)
        self.repodirector = DirectorRepository(db)

    def create_film(self, film_data: FilmCreate):
        # Exemplo de regra de negócio: duração mínima
        if film_data.duration <= 0:
            raise HTTPException(status_code=422, detail="A duração do filme deve ser maior que zero.")

        if not self.repocatory.get_by_id(film_data.category_id):
            raise HTTPException(status_code=404, detail="A categoria selecionada não existe.")
        
        if not self.repodirector.get_by_id(film_data.director_id):
            raise HTTPException(status_code=404, detail="O diretor selecionadol não existe.")



        return self.repofilm.create(film_data)

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
        return self.repofilm.list_all(
            skip=skip,
            limit=page_size,
            title=title,
            category=category,
            language=language,
            release_year=release_year
        )

    def get_film(self, film_id: int):
        film = self.repofilm.get_by_id(film_id)
        if not film:
            raise ValueError("Filme não encontrado.")
        return film

    def update_film(self, film_id: int, film_data: FilmCreate):
        film = self.repofilm.update(film_id, film_data)
        if not film:
            raise HTTPException(status_code=404, detail="Filme não encontrado.")
        
        if not self.repocatory.get_by_id(film_data.category_id):
            raise HTTPException(status_code=404, detail="A categoria selecionada não existe.")
        
        if not self.repodirector.get_by_id(film_data.director_id):
            raise HTTPException(status_code=404, detail="O diretor selecionadol não existe.")
        return film

    def delete_film(self, film_id: int):
        film = self.repofilm.delete(film_id)
        if not film:
            raise HTTPException(status_code=404, detail="Filme não encontrado")
        return film
