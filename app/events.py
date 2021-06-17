import typing
import app.db.preload as database_preload

def create_start_app_handler() -> typing.Callable:
	async def start_app() -> None:
		database_preload.load()

	return start_app