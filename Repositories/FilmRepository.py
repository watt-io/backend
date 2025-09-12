from sqlalchemy.orm import Session
from Models.FilmModel import Film
from DTOs.FilmDTOs import FilmCreate

class FilmRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, film_data: FilmCreate) -> Film:
        film = Film(**film_data.dict())
        self.db.add(film)
        self.db.commit()
        self.db.refresh(film)
        return film

    def list_all(
        self,
        skip: int = 0, limit: int = 10,
        title: str | None = None,
        category: str | None = None,
        language: str | None = None,
        release_year: int | None = None
    ):
        query = self.db.query(Film)

        if title:
            query = query.filter(Film.title.ilike(f"%{title}%"))
        if category:
            query = query.filter(Film.category == category)
        if language:
            query = query.filter(Film.language == language)
        if release_year:
            query = query.filter(Film.release_year == release_year)

        return query.offset(skip).limit(limit).all()

    def get_by_id(self, film_id: int):
        return self.db.query(Film).filter(Film.id == film_id).first()

    def update(self, film_id: int, film_data: FilmCreate):
        film = self.get_by_id(film_id)
        if film:
            for field, value in film_data.dict().items():
                setattr(film, field, value)
            self.db.commit()
            self.db.refresh(film)
        return film
    
    def delete(self, film_id: int):
        film = self.get_by_id(film_id)
        if film:
            self.db.delete(film)
            self.db.commit()
        return film
