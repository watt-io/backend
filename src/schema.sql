CREATE DATABASE IF NOT EXISTS movie_db;

CREATE TABLE IF NOT EXISTS movies(
    id SERIAL PRIMARY KEY,
    movieName TEXT NOT NULL,
    synopsis TEXT,
    duration INT,
    yearRelease INT,
    movie_gender TEXT
);