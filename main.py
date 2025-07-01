from models.movie import MovieModel
from database.connection import get_connection
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

@app.get('/filmes/{id}')
def get_one_movie(id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
        SELECT id, movie_name, synopsis, duration, year_release, movie_gender
        FROM movies
        WHERE id = %s;
    ''', (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        movie = {
            'id': row[0],
            'movie_name': row[1],
            'synopsis': row[2],
            'duration': row[3],
            'year_release': row[4],
            'movie_gender': row[5],
        }
        return movie
    
    else:
        raise HTTPException(status_code=404, detail='Filme não encontrado :(')

@app.get('/filmes')
def get_all_movies():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
        SELECT id, movie_name, synopsis, duration, year_release, movie_gender
        FROM movies;
    ''')
    rows = cur.fetchall()

    cur.close()
    conn.close()

    movies = []
    for row in rows:
        movies.append({
            'id': row[0],
            'movie_name': row[1],
            'synopsis': row[2],
            'duration': row[3],
            'year_release': row[4],
            'movie_gender': row[5],
        })

    return movies
