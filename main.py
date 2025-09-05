from fastapi import FastAPI;
app = FastAPI()

from routes import routes
app.include_router(routes)


# Rodar o servidor: uvicorn main:app --reload
