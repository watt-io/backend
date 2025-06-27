from fastapi import FastAPI
from adapters.driver.api.routes import router

app = FastAPI()
app.include_router(router)
