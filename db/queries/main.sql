CREATE DATABASE tournament;

USE tournament;

/* BASIC TABLES */

CREATE TABLE clubs(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL
);

CREATE TABLE coaches(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    birth CHAR(4)
);

CREATE TABLE players(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    position CHAR(2),
    birth CHAR(4),
    height FLOAT,
    weight FLOAT,
    foot CHAR(1)
);

CREATE TABLE stadiums(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    capacity INT
);

/* RELATIONS */

CREATE TABLE player_contracts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    start CHAR(4) NOT NULL,
    end CHAR(4) NOT NULL,
    transfer_amount INT,
    salary INT NOT NULL,
    termination_fine INT,
    club_id INT,
    FOREIGN KEY (club_id) 
        REFERENCES clubs(id),
    player_id INT,
    FOREIGN KEY (player_id) 
        REFERENCES players(id)  
);

CREATE TABLE coach_contracts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    start CHAR(4) NOT NULL,
    end CHAR(4) NOT NULL,
    salary INT NOT NULL,
    termination_fine INT,
    club_id INT,
    FOREIGN KEY (club_id) 
        REFERENCES clubs(id),
    coach_id INT,
    FOREIGN KEY (coach_id) 
        REFERENCES coaches(id)  
);

CREATE TABLE stats(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    matches INT,
    goals INT,
    assists INT,
    tackles INT,
    clearences INT,
    stolen_balls INT,
    clean_sheets INT,
    defenses INT,
    difficult_defenses INT,
    goals_conceded INT,
    player_id INT,
    FOREIGN KEY (player_id) 
        REFERENCES players(id)  
);

CREATE TABLE market_value(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    value INT,
    player_id INT,
    FOREIGN KEY (player_id) 
        REFERENCES players(id)
);

/* CHAMPIONSHIPS 
Divison -> Competition -> Championships[table that stores all year competition] -> Champions

*/


CREATE TABLE competitions(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE divisons(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    competition_id INT,
    FOREIGN KEY(competition_id)
        REFERENCES competitions(id)
);

CREATE TABLE championships(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    matches INT,
    won INT,
    draw INT,
    lost INT,
    goals_for INT,
    goals_away INT,
    goall_diff INT,
    club_id INT,
    FOREIGN KEY (club_id) 
        REFERENCES clubs(id),
    divison_id INT,
    FOREIGN KEY (divison_id)
        REFERENCES divisons(id)
);

CREATE TABLE champions(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    
    season CHAR(4) NOT NULL,
    club_id INT,
    FOREIGN KEY (club_id) 
        REFERENCES clubs(id),
    competition_id INT,
    FOREIGN KEY(competition_id)
        REFERENCES competitions(id)
);
