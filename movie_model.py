class Movie(object):
    """docstring for Movie."""

    def __init__(self, id: int, name: str, year: int, cast: list, genre: str, director: str):
        self.id = id
        self.name = name
        self.year = year
        self.cast = cast
        self.genre = genre
        self.director = director

    def return_dic(self):
        return {"id":self.id,"name":self.name,"year":self.year,"cast":self.cast,"genre":self.genre,"director":self.director}


movie1 = Movie(1, "Homem Aranha", 2021, ["Tom Holland", "Zendaya", "Benedic"], "Action", "Jon Watts")

json = movie1.return_dic()

print(json)
