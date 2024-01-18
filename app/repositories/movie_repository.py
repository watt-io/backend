from fastapi import HTTPException
import mysql.connector
from app.models.movie import Movie, MovieData

class MovieRepository:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def createMovie(self, movie: Movie):
        query = "INSERT INTO movies (title, year, genre) VALUES (%s, %s, %s)"
        values = (movie.title, movie.year, movie.genre)

        self.cursor.execute(query, values)
        self.conn.commit()
        movieId = self.cursor.lastrowid
        return MovieData(id=movieId, title=movie.title, year=movie.year, genre=movie.genre)

    def getMovies(self):
        query = "SELECT * FROM movies"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        movies = []

        if result is None:
            raise HTTPException(status_code=404, detail="No movies found")
        
        for movieData in result:
            movie = MovieData(id=movieData[0], title=movieData[1], year=movieData[2], genre=movieData[3])
            movies.append(movie)

        return movies

    def getMovieById(self, movieId: int):
        query = "SELECT * FROM movies WHERE id = %s"
        values = (movieId,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Movie not found")

        return MovieData(id=result[0], title=result[1], year=result[2], genre=result[3])
    
    def deleteMovie(self, movieId: int):

        movieToDelete = self.getMovieById(movieId)
        if movieToDelete:
            query = "DELETE FROM movies WHERE id = %s"
            values = (movieId,)
            self.cursor.execute(query, values)

        return movieToDelete
    
    def updateMovie(self, updatedMovie: MovieData):

        movieId = updatedMovie.id
        movieToUpdate = self.getMovieById(movieId)
        
        if movieToUpdate:
            query = "UPDATE movies SET title=%s, year=%s, genre=%s WHERE id=%s"
            values = (updatedMovie.title, updatedMovie.year, updatedMovie.genre, movieId)
            self.cursor.execute(query, values)
            self.conn.commit()

        return updatedMovie
