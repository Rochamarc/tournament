CREATE TABLE players(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    age INT NOT NULL, 
    position CHAR(2) NOT NULL,
    height FLOAT NOT NULL,
    weight FLOAT NOT NULL,
    foot CHAR(1) NOT NULL
);