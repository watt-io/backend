import json

def test_add_movie_success(test_app):
	test_request_payload = {"id": "18c2", "title": "The Benchwarmers", "genre": "comedy", "release": "2006", "imdb": 7.8}
	test_response_payload = {"data":[{"id":"18c2","title":"The Benchwarmers","genre":"comedy","release":"2006","imdb":7.8}],"code":200,"message":"Movie added successfully."}

	response = test_app.post("/filmes/", json=test_request_payload)

	assert response.status_code == 200
	assert response.json() == test_response_payload

def test_add_movie_invalid_json(test_app):
	test_request_payload = {"id": "18c2", "title": "The Benchwarmers", "genre": "comedy", "release": "2006"}
	test_response_payload = {"detail": [{"loc": ["body", "imdb"], "msg": "field required", "type": "value_error.missing"}]}

	response = test_app.post("/filmes/", json=test_request_payload)

	assert response.status_code == 422
	assert response.json() == test_response_payload

def test_retrieve_movies(test_app):
	test_response_payload = {
		"data": [
			{"id": "9207", "title": "The Week Of", "genre": "comedy", "release": "2018", "imdb": 5.2},
			{"id": "6532", "title": "The Ridiculous 6", "genre": "action/comedy", "release": "2015", "imdb": 4.8},
			{"id": "0c22", "title": "Sandy Wexler", "genre": "comedy", "release": "2017", "imdb": 5.2},
			{"id": "8364", "title": "You Don't Mess with the Zohan", "genre": "comedy", "release": "2008", "imdb": 5.5},
			{"id": "18c2", "title": "The Benchwarmers", "genre": "comedy", "release": "2006", "imdb": 7.8}
		],
		"code": 200,
		"message": "Movies data retrieved successfully."
	}

	response = test_app.get("/filmes/")

	assert response.status_code == 200
	assert response.json() == test_response_payload

def test_retrieve_movie(test_app):
	test_response_payload = {
		"data": [{
			"id": "8364",
			"title": "You Don't Mess with the Zohan",
			"genre": "comedy",
			"release": "2008",
			"imdb": 5.5
		}],
		"code": 200,
		"message": "Movie data retrieved successfully."
	}

	response = test_app.get("/filmes/8364")

	assert response.status_code == 200
	assert response.json() == test_response_payload

def test_retrieve_movie_invalid_id(test_app):
	response = test_app.get("/filmes/0x00")

	assert response.status_code == 404
	assert response.json()["message"] == "Movie not found."