from fastapi import APIRouter
from src.api.routes.filmes import router as filmes_router

router= APIRouter()

router.include_router(filmes_router, prefix="/filmes", tags=["filmes"])