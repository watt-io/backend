from fastapi import FastAPI # Importing framework for API use
from Movie import * 

# Creating API ( uvicorn [File name]:[API Object name] --reload)
app = FastAPI()

# Dictionary with movies in DB 
movie1 = Movie()
movie1.setMovieId(0)
movie1.setMovieName('Harry Potter e a Pedra Filosofal')
movie1.setMovieGenre('Fantasia/Aventura')
movie1.setMovieLength('152 minutos')
movie1.setMovieRelease('2001')

movie2 = Movie()
movie2.setMovieId(1)
movie2.setMovieName('Harry Potter e a Câmara Secreta')
movie2.setMovieGenre('Fantasia/Aventura')
movie2.setMovieLength('161 minutos')
movie2.setMovieRelease('2002')

movies = {
    movie1.getMovieId(): movie1,
    movie2.getMovieId(): movie2
}


# Route Definition to define app functionalities



@app.get('/')
def homePage():
    return {'Filmes No Catálogo:' : len(movies)}

@app.get('/filmes')
def getMovies():
    for movie in movies:
        return movies
    
@app.post('/filmes')
def postMovie(name: str, length: str, genre: str, release: str):
    newMovie = Movie() # Create a new movie to be added
    newMovie = Movie()
    newMovie.setMovieId(len(movies)) # Define movie Id as the last in the list
    newMovie.setMovieName(name)
    newMovie.setMovieGenre(genre)
    newMovie.setMovieLength(length)
    newMovie.setMovieRelease(release)
    movies[newMovie.getMovieId()] = newMovie
    
@app.get('/filmes/{id}')
def getmovies(id: int):
    if(id in movies):
        return movies[id] # If movie Id is in the list, it returns the movie
    else:
        return {'Filme não está na lista'}
    


