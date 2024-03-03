from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def pagina_inicial():
    return {"Olá FastAPI": "Olá FastAPI"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
