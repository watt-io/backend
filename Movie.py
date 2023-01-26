class Movie:
    def __init__(self): # Movie class constructor
        self.movieId = None
        self.movieName = None
        self.movieLength = None
        self.movieGenre = None
        self.movieRelease = None

#region gets n sets
    
    # Movie id   
    def setMovieId(self, movieId):
        self.movieId = movieId
        
    def getMovieId(self):
        return self.movieId
    
    # Movie name
    def setMovieName(self, movieName):
        self.movieName = movieName
        
    def getMovieName(self):
        return self.movieName
    
    # Movie length
    def setMovieLength(self, movieLength):
        self.movieLength = movieLength
        
    def getMovieLength(self):
        return self.movieLength
    
    # Movie genre
    def setMovieGenre(self, movieGenre):
        self.movieGenre = movieGenre
        
    def getMovieGenre(self):
        return self.movieGenre
    
    # Movie release
    def setMovieRelease(self, movieRelease):
        self.movieRelease = movieRelease
        
    def getmovieRelease(self):
        return self.movieRelease
#endregion
