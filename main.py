from src.model import MovieModel
from src.db import get_connection
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('/filmes')
def register_movie(movie: MovieModel):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO movies (movie_name, synopsis, duration, year_release, movie_gender)
        VALUES (%s, %s, %s, %s, %s);
    ''', (movie.movie_name, movie.synopsis, movie.duration, movie.year_release, movie.movie_gender))

    conn.commit()
    cur.close()
    conn.close()

    return {'Mensagem': 'Filme cadastrado com sucesso!'}

# @app.get('/filmes/{id}')
# def get_one_movie(id: int):
#     for movie in movies_db:
#         if movie.id == id:
#             return movie
#     HTTPException(status_code=404, detail='Filme não encontrado :(')

# @app.get('/filmes')
# def get_all_movies():
#     return movies_db
