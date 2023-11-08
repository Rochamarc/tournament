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
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100),
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


CREATE TABLE games(
    id INT PRIMARY KEY AUTO_INCREMENT,
    season CHAR(4) NOT NULL,
    hour CHAR(5) NOT NULL,
    climate VARCHAR(5),
    weather VARCHAR(10),
    stadium VARCHAR(100) NOT NULL,
    audience INT,
    ticket_value INT,
    home_game_stats_id INT,
    away_game_stats_id INT
);


CREATE TABLE game_stats(
    id INT PRIMARY KEY AUTO_INCREMENT,         
    goals INT DEFAULT 0,           
    shots INT DEFAULT 0,           
    shots_on_target INT DEFAULT 0, 
    fouls INT DEFAULT 0,           
    tackles INT DEFAULT 0,
    stolen_balls INT DEFAULT 0,
    saves INT DEFAULT 0,           
    ball_possession INT DEFAULT 0, 
    offsides INT DEFAULT 0,        
    freekicks INT DEFAULT 0,       
    penalties INT DEFAULT 0,       
    club_id INT DEFAULT 0
);

CREATE TABLE championships(
    id INT PRIMARY KEY AUTO_INCREMENT,
    season CHAR(4) NOT NULL,
    matches INT DEFAULT 0,
    win INT DEFAULT 0,
    loss INT DEFAULT 0,
    draw INT DEFAULT 0,
    goals_for INT DEFAULT 0,
    goals_away INT DEFAULT 0,
    goals_diff INT DEFAULT 0,
    points INT DEFAULT 0,
    division_id INT,
    club_id INT
);

/* PLAYER SKILL 

sliding_tackle
shooting
strength
vision

short_passing
long_passing

marking

penalties
*/

CREATE TABLE skills(
    id INT PRIMARY KEY AUTO_INCREMENT,
    season CHAR(4) NOT NULL,
    positioning INT DEFAULT 0,
	reflexes INT DEFAULT 0,
	diving INT DEFAULT 0,
	standing_tackle INT DEFAULT 0,
	physical INT DEFAULT 0,
	passing INT DEFAULT 0,
    dribbling INT DEFAULT 0,
	long_shot INT DEFAULT 0,
	finishing INT DEFAULT 0,
	player_id INT
);

CREATE TABLE competitions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE divisions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    competition_id INT
);

CREATE TABLE stadium_ownership(
    id INT PRIMARY KEY AUTO_INCREMENT,
    club_id INT,
    stadium_id INT
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

ALTER TABLE games
ADD CONSTRAINT fk_games_home_game_stats
FOREIGN KEY(home_game_stats_id)
REFERENCES game_stats(id);

ALTER TABLE games
ADD CONSTRAINT fk_games_away_game_stats
FOREIGN KEY(away_game_stats_id)
REFERENCES game_stats(id);

ALTER TABLE game_stats 
ADD CONSTRAINT fk_game_stats_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE championships 
ADD CONSTRAINT fk_championship_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE championships
ADD CONSTRAINT fk_championship_divisions
FOREIGN KEY(division_id)
REFERENCES divisions(id);

ALTER TABLE divisions 
ADD CONSTRAINT fk_division_competitions
FOREIGN KEY(competition_id)
REFERENCES competitions(id);

ALTER TABLE stadium_ownership
ADD CONSTRAINT fk_stadium_ownership_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE stadium_ownership
ADD CONSTRAINT fk_stadium_ownership_stadiums
FOREIGN KEY(stadium_id)
REFERENCES stadiums(id);

ALTER TABLE skills
ADD CONSTRAINT fk_skills_players
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