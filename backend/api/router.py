from fastapi import APIRouter
from api.routes import (
    auth_v1, 
    film_v1,
    user_v1,
)

router = APIRouter()

router.include_router(auth_v1.router, prefix='/auth', tags=['Auth'], include_in_schema=False)
router.include_router(film_v1.router, prefix='/filmes', tags=['Filmes'])
router.include_router(user_v1.router, prefix='/usuarios', tags=['Usuários'])
