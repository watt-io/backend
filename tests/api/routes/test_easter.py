def test_easter(test_app):
	response = test_app.get("/easter/")
	assert response.status_code == 200
	assert response.json() == {
		"body": "Have you notice that all preloaded movies are from Adam Sandler ?",
		"answer": "I guess not! Gotcha!"
	}