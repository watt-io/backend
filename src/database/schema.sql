CREATE TABLE IF NOT EXISTS movies(
    id SERIAL PRIMARY KEY,
    movie_name TEXT NOT NULL UNIQUE,
    synopsis TEXT,
    duration INT,
    year_release INT,
    movie_gender TEXT
);