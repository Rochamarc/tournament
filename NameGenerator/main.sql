CREATE DATABASE tournament_name;

USE tournament_name;

CREATE TABLE first_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(100) NOT NULL,
    nationality VARCHAR(100)
);

CREATE TABLE last_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(100) NOT NULL,
    nationality VARCHAR(100)
);

