/* DATABASE */

CREATE DATABASE tournament;

USE tournament;

/* TABLES */

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

CREATE TABLE player_contracts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    start CHAR(4) NOT NULL,
    end CHAR(4) NOT NULL,
    transfer_amount INT,
    salary INT NOT NULL,
    termination_fine INT,
    club_id INT,
    player_id INT
);

CREATE TABLE coach_contracts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    start CHAR(4) NOT NULL,
    end CHAR(4) NOT NULL,
    salary INT NOT NULL,
    termination_fine INT,
    club_id INT,
    coach_id INT
);

CREATE TABLE stats(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    matches INT DEFAULT 0,
    goals INT DEFAULT 0,
    assists INT DEFAULT 0,
    tackles INT DEFAULT 0,
    clearences INT DEFAULT 0,
    stolen_balls INT DEFAULT 0,
    clean_sheets INT DEFAULT 0,
    defenses INT DEFAULT 0,
    difficult_defenses INT DEFAULT 0,
    goals_conceded INT DEFAULT 0,
    player_id INT
);

CREATE TABLE market_value(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    value INT,
    player_id INT    
);


CREATE TABLE overall(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    overall INT NOT NULL,
    player_id INT
);

/* RETIRING AND BACKUPS */

CREATE TABLE retired_players(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_player INT,    
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    position CHAR(2),
    birth CHAR(4),
    foot CHAR(1)
);

/* CONSTRAINTS */

ALTER TABLE player_contracts
ADD CONSTRAINT fk_player_contracts_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE player_contracts
ADD CONSTRAINT fk_player_contracts_coaches
FOREIGN KEY(player_id)
REFERENCES players(id);

ALTER TABLE coach_contracts
ADD CONSTRAINT fk_coach_contracts_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE coach_contracts
ADD CONSTRAINT fk_coach_contracts_coaches
FOREIGN KEY(coach_id)
REFERENCES coaches(id);

ALTER TABLE stats 
ADD CONSTRAINT fk_stats_players
FOREIGN KEY(player_id)
REFERENCES players(id);

ALTER TABLE market_value 
ADD CONSTRAINT fk_market_value_players
FOREIGN KEY(player_id)
REFERENCES players(id);

ALTER TABLE overall
ADD CONSTRAINT fk_overall_players
FOREIGN KEY(player_id)
REFERENCES players(id);

/* ADD TRIGGERS */

DELIMITER $

CREATE TRIGGER rtr_players 
BEFORE DELETE ON players 
FOR EACH ROW
BEGIN 
    INSERT INTO retired_players VALUES(NULL, OLD.id, OLD.name, OLD.nationality, OLD.position, OLD.birth, OLD.foot);
END
$

DELIMITER ;