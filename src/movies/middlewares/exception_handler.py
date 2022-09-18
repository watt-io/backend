from httpx import HTTPStatusError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse


async def generic_request_exception_handler(request: Request, exc: HTTPStatusError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={'message': str(exc)})


async def exception_repository(request: Request, exc: HTTPStatusError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': str(exc)})


async def exception_repository_not_found(request: Request, exc: HTTPStatusError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': str(exc)})
