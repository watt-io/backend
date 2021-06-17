from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel
from core.databases import Connection
from fastapi import Depends, APIRouter, HTTPException
import secrets
from .auth_v1 import get_current_user

router = APIRouter()


class FilmIn(BaseModel):
    title: str
    director: str
    release_on: date


class FilmOut(BaseModel):
    id: int
    title: str
    director: str
    release_on: date
    is_deleted: bool
    inserted_on: datetime
    updated_on: Optional[datetime]=None


@router.post('/')
async def create_film(data: FilmIn, user=Depends(get_current_user)):
    """
    Cadastrar um novo filme
    """
    try:
        args = [data.title, data.director, data.release_on]
        with Connection() as db:
            sql = '''
                INSERT INTO film
                (title, director, release_on) VALUES 
                (%s, %s, %s)
                RETURNING id
            '''
            result = db.query_dict(sql, args)
            id = result[0].get('id') if result else None
        return {'ok': True, 'id': id}
    except:
        raise HTTPException(400, 'Bad Request')


@router.get('/', response_model=List[FilmOut])
async def read_all_films(user=Depends(get_current_user)):
    """
    Retornar dados de todos os filmes cadastrados
    """
    try:
        with Connection() as db:
            sql = '''
                SELECT *
                FROM film
                WHERE 1 = 1
                  AND is_deleted = 0
            '''
            result = db.query_dict(sql)
        films = result if result else []
        return films
    except:
        raise HTTPException(400, 'Bad Request')


@router.get('/{id}', response_model=FilmOut)
async def read_film(id: int, user=Depends(get_current_user)):
    """
    Filtrar filme buscando ID específico passado via *path parameters*
    """
    try:
        with Connection() as db:
            sql = '''
                SELECT *
                FROM film
                WHERE 1 = 1
                  AND is_deleted = 0
                  AND id = %s
            '''
            result = db.query_dict(sql, [id])
        film = result[0] if result else None
        return film
    except:
        raise HTTPException(400, 'Bad Request')


@router.put('/{id}')
async def update_film(id: int, data: FilmIn, user=Depends(get_current_user)):
    """
    Atualiza um filme já cadastrado
    """
    try:
        args = [data.title, data.director, data.release_on, id]
        with Connection() as db:
            sql = '''
                UPDATE film
                SET updated_on = NOW(),
                    title = %s,
                    director = %s,
                    release_on = %s
                WHERE is_deleted = 0
                  AND id = %s
            '''
            db.execute(sql, args)
        return {'ok': True}
    except:
        raise HTTPException(400, 'Bad Request')


@router.delete('/{id}')
async def delete_filme(id: int, user=Depends(get_current_user)):
    """
    Realizar a **deleção lógica** de um filme específico
    """
    try:
        with Connection() as db:
            sql = '''
                UPDATE film
                SET is_deleted = 1
                WHERE id = %s
            '''
            db.execute(sql, [id])
        return {'ok': True} 
    except:
        raise HTTPException(400, 'Bad Request')
