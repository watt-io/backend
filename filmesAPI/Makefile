install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt
migration:
	python manage.py migrate &&\
		python manage.py makemigrations filmes
lint:
	pylint --disable=R,C *.py
test:
	#test
build:
	docker build -t filmes_api .
run:
	docker run -p 8000:8000 --rm filmes_api:latest
deploy:
	#deploy
all:
	install lint test deploy