import fastapi

from app.api.routes import router
from app.events import create_start_app_handler

def initialize_app() -> fastapi.FastAPI:
	app = fastapi.FastAPI(title='WATTIO Coding Test', version="0.0.1")

	app.add_event_handler('startup', create_start_app_handler())
	app.include_router(router.routes)

	return app

app = initialize_app()