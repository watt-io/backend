import logging
import time
from fastapi import FastAPI, Request

# Configuração do logging
logging.basicConfig(
    filename="app.log",        # arquivo de log
    level=logging.INFO,         # nível de log
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("app")


async def log_requests(request: Request, call_next):
    start_time = time.time()
    try:
        # Log da requisição (sem corpo)
        logger.info(f"Requisição recebida: {request.method} {request.url}")

        response = await call_next(request)

        # Log da resposta
        duration = time.time() - start_time
        logger.info(f"Requisição finalizada: {request.method} {request.url} - {response.status_code} - {duration:.3f}s")

        return response

    except Exception as e:
        # Log de erros com traceback
        logger.error(f"Erro na requisição: {request.method} {request.url} - {str(e)}", exc_info=True)
        raise
