from sqlalchemy.orm.session import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db : Session):
    films = db.query(models.Filme).all()
    return films

def insert(request: schemas.Filme, db: Session):
    new_film = models.Filme(
        nome=request.nome, 
        ano=request.ano, 
        categoria=request.categoria,
        user_id=1
        )
    db.add(new_film)
    db.commit()
    db.refresh(new_film)

    return new_film

def get(id: int, db: Session):
    film_id = db.query(models.Filme).filter(models.Filme.id == id).first()
    if not film_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    return film_id

def delete(id: int, db: Session):
    filme_del = db.query(models.Filme).filter(models.Filme.id == id)
    if not filme_del.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    filme_del.delete(synchronize_session=False)
    db.commit()
    return {'detail':'Done'}