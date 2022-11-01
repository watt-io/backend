FROM python:3.8

WORKDIR /DockerMovieDB

COPY . .

RUN pip install -r ./requirements.txt

