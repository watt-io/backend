USE db;

CREATE TABLE user (
  id INTEGER NOT NULL AUTO_INCREMENT,
  username VARCHAR(30) UNIQUE NOT NULL,
  password VARCHAR(70) NOT NULL,
  is_active TINYINT(1) NOT NULL DEFAULT 1,
  last_login DATETIME DEFAULT NULL,
  inserted_on DATETIME DEFAULT NOW(),
  PRIMARY KEY(id)
);

CREATE TABLE film (
  id INTEGER NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  director VARCHAR(100) NOT NULL,
  release_on DATETIME NOT NULL,
  inserted_on DATETIME NOT NULL DEFAULT NOW(),
  updated_on DATETIME,
  PRIMARY KEY(id)
);


/*
  ! Popular tabela exemplo
  username: admin
  password: admin
*/
INSERT INTO
  user (username, password)
VALUES
  (
    'admin',
    '$2b$12$e.L97G95MrCQpta7SBTEkeyRAqPeUMdTkTp3pugkseTy9Q7Fqy6XS'
  );
