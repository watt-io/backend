import typing
import app.db.preload as database_preload

def create_start_app_handler() -> typing.Callable: # type: ignore
	async def start_app() -> None:
		await database_preload.load()

	return start_app