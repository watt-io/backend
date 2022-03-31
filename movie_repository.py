import json
from movie_model import Movie

class Repository:

    # CRUD --------------------------------------
    def save_item(self, id: str, name: str, year: int, cast: list, genre: str, director: str):
        movie = Movie(id, name, year, cast, genre, director)
        dict_to_add = {movie.get_id() : movie.return_dict()} #cria um dictionary com o dict_movie como o value da key ["id"]
        with open('data.json','r+') as file:
            print("entrei")
            file_data = json.load(file)
            file_data.update(dict_to_add)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

    def read_items(self):
        with open('data.json', 'r') as openfile:
            json_object = json.load(openfile)
        return json_object

    def read_by_id(self, id : str):
        with open('data.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object[id]

    def update_item(self, id: str, key : str, value):
        if key == "cast":
            value = list(value.split(", "))
        with open('data.json', 'r') as openfile:
            json_object = json.load(openfile)
            json_object[id][key] = value
        with open("data.json", "w") as outfile:
            outfile.write(json.dumps(json_object, indent = 4))

    def delete_item(self, id: str):
        with open('data.json', 'r') as openfile:
            json_object = json.load(openfile)
            del json_object[id]
        with open("data.json", "w") as outfile:
            outfile.write(json.dumps(json_object, indent = 4))
