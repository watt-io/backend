import fastapi

from . import (
	filmes,
	easter
)

routes = fastapi.APIRouter()
routes.include_router(filmes.router, tags=["movies"])
routes.include_router(easter.router, tags=["comedy"])