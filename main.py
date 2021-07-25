from fastapi import FastAPI

app = FastAPI()

@app.get('/filmes')
async def get_all_movies():
    return {"filme":"EX MACHINA"}

@app.post('/filmes')
async def create_movie():
    return {"id":"teste"}