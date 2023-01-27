from  Client import *


class Movie(): 
    def __init__(self, id): # Movie class constructor
        self.movieId = id
        self.movieName = None
        self.movieLength = None
        self.movieGenre = None
        self.movieRelease = None
        self.movieRentedBy = None

#region gets n sets
    
    # Movie id   
    def getMovieId(self):
        return self.movieId
    
    # Movie name
    def setMovieName(self, movieName:str):
        self.movieName = movieName
        
    def getMovieName(self):
        return self.movieName
    
    # Movie length
    def setMovieLength(self, movieLength:str):
        self.movieLength = movieLength
        
    def getMovieLength(self):
        return self.movieLength
    
    # Movie genre
    def setMovieGenre(self, movieGenre:str):
        self.movieGenre = movieGenre
        
    def getMovieGenre(self):
        return self.movieGenre
    
    # Movie release
    def setMovieRelease(self, movieRelease:str):
        self.movieRelease = movieRelease
        
    def getmovieRelease(self):
        return self.movieRelease
    
    # Movie rented by
    def setMovieRentedBy(self, movieRentedBy:Client):
        self.movieRentedBy = movieRentedBy
    
    def getMovieRentedBy(self):
        return self.movieRentedBy
#endregion
