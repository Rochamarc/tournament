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

CREATE TABLE overall(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    overall INT NOT NULL,
    player_id INT,
    FOREIGN KEY(player_id)
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
    matches INT DEFAULT 0,
    won INT DEFAULT 0,
    draw INT DEFAULT 0,
    lost INT DEFAULT 0,
    goals_for INT DEFAULT 0,
    goals_away INT DEFAULT 0,
    goall_diff INT DEFAULT 0,
    points INT DEFAULT 0,
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

/* NAMING */

CREATE TABLE first_names(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    value VARCHAR(100) NOT NULL,
    language VARCHAR(100) NOT NULL
);

CREATE TABLE last_names(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    value VARCHAR(100) NOT NULL,
    language VARCHAR(100) NOT NULL
);

/* GAMES TABLES 

hour -> 00:00 -> char(5)

*/

CREATE TABLE home_game_stats (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goals INT,
    shots INT,
    shots_on_target INT,
    fouls INT,
    tackles INT,
    saves INT,
    ball_possession INT,
    offsides INT,
    freekicks INT,
    penalties INT,
    club_id INT,
    FOREIGN KEY (club_id)
        REFERENCES clubs(id)
);

CREATE TABLE away_game_stats (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goals INT,
    shots INT,
    shots_on_target INT,
    fouls INT,
    tackles INT,
    saves INT,
    ball_possession INT,
    offsides INT,
    freekicks INT,
    penalties INT,
    club_id INT,
    FOREIGN KEY (club_id)
        REFERENCES clubs(id)
);

CREATE TABLE games (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    hour CHAR(5),
    home_game_id INT NOT NULL,
    FOREIGN KEY(home_game_id)
        REFERENCES home_game_stats(id),
    away_game_id INT NOT NULL,
    FOREIGN KEY(home_game_id)
        REFERENCES away_game_stats(id)
);