import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from httpx import HTTPStatusError

from exception import ValidationException, RepositoryException, RepositoryNotFoundException
from movies.middlewares.exception_handler import generic_request_exception_handler, exception_repository, \
    exception_repository_not_found


def create_app() -> False:
    app = FastAPI()
    from movies.infrastructure.containers import Container
    container = Container()

    from movies.endpoints.movies import controller as movies_module
    movies_module.configure(app)

    container.wire(modules=[movies_module])

    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'],
                       allow_headers=['*'])

    app.add_exception_handler(ValidationException, handler=generic_request_exception_handler)
    app.add_exception_handler(RepositoryException, handler=exception_repository)
    app.add_exception_handler(RepositoryNotFoundException, handler=exception_repository_not_found)
    app.add_exception_handler(HTTPStatusError, handler=generic_request_exception_handler)

    app.container = container

    return app


api_app = create_app()

if __name__ == '__main__':
    uvicorn.run(api_app, host='0.0.0.0', port=8081)
