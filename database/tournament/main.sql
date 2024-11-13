/* DATABASE */

/* TABLES */
USE Tournament;

ALTER DATABASE `Tournament` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE club_classes(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name CHAR(1)
);

CREATE TABLE clubs(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    club_class_id INT
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

/*  Change this not null to null to adapt this   
    to FREE AGENT 
*/

CREATE TABLE player_contracts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    start CHAR(4),
    end CHAR(4),
    transfer_amount INT,
    salary INT,
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
    shots INT DEFAULT 0,
    shots_on_target INT DEFAULT 0,
    goals INT DEFAULT 0,
    assists INT DEFAULT 0,
    fouls_committed INT DEFAULT 0,
    tackles INT DEFAULT 0,
    passes INT DEFAULT 0,
    wrong_passes INT DEFAULT 0,
    intercepted_passes INT DEFAULT 0,
    clearances INT DEFAULT 0,
    stolen_balls INT DEFAULT 0,
    clean_sheets INT DEFAULT 0,
    defenses INT DEFAULT 0,
    difficult_defenses INT DEFAULT 0,
    goals_conceded INT DEFAULT 0,
    player_id INT,
    game_id INT
);

CREATE TABLE market_value(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    value INT,
    player_id INT    
);

CREATE TABLE retired_players(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_player INT,    
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    position CHAR(2),
    birth CHAR(4),
    foot CHAR(1)
);

-- TODO add competition ind on games

CREATE TABLE games(
    id INT PRIMARY KEY AUTO_INCREMENT,
    season CHAR(4) NOT NULL,
    hour CHAR(5) NOT NULL,
    climate VARCHAR(5),
    weather VARCHAR(10),
    stadium VARCHAR(100) NOT NULL,
    audience INT,
    ticket_value INT,
    competition_id INT,
    home_game_stats_id INT,
    away_game_stats_id INT
);


CREATE TABLE game_stats(
    id INT PRIMARY KEY AUTO_INCREMENT,         
    goals INT DEFAULT 0,           
    shots INT DEFAULT 0,           
    shots_on_target INT DEFAULT 0, 
    fouls INT DEFAULT 0,           
    passes INT DEFAULT 0,
    wrong_passes INT DEFAULT 0,
    interceptions INT DEFAULT 0,
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


CREATE TABLE player_game_stats(
	id INT PRIMARY KEY AUTO_INCREMENT,
	assists INT DEFAULT 0,
	goals INT DEFAULT 0,
	tackles INT DEFAULT 0,
	defenses INT DEFAULT 0,
	passes INT DEFAULT 0,
	wrong_passes INT DEFAULT 0,
	intercepted_passes INT DEFAULT 0,
	dificult_defenses INT DEFAULT 0,
	clearances INT DEFAULT 0,
	fouls_committed INT DEFAULT 0,
	stolen_balls INT DEFAULT 0,
	player_id INT,
	game_id INT	
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


CREATE TABLE group_phase(
    id INT PRIMARY KEY AUTO_INCREMENT,
	group_name CHAR(1) NOT NULL,
    season CHAR(4) NOT NULL,
    matches INT DEFAULT 0,
    win INT DEFAULT 0,
    loss INT DEFAULT 0,
    draw INT DEFAULT 0,
    goals_for INT DEFAULT 0,
    goals_away INT DEFAULT 0,
    goals_diff INT DEFAULT 0,
    points INT DEFAULT 0,
    club_id INT,
    competition_id INT
);


/* NEW SYSTEM 

now 
    home_id -> games
    away_id -> games
    home_game_stats_id -> games
    away_games_stats_id -> games
    season -> games
    penalties -> penalties
    home_penalties -> penalties
    away_penalties -> penalties
*/

CREATE TABLE qualifiers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    season CHAR(4) NOT NULL,
    phase VARCHAR(100) NOT NULL,
    club_id INT,
    competition_id INT
);

CREATE TABLE knock_out(
    id INT PRIMARY KEY AUTO_INCREMENT,
    phase VARCHAR(50) NOT NULL,
    single_match BOOLEAN NOT NULL,
    match_number INT NOT NULL,
    game_id INT,
    penalty_id INT
);

CREATE TABLE penalties(
    id INT PRIMARY KEY AUTO_INCREMENT,
    penalties BOOLEAN NOT NULL,
    home_penalties INT,
    away_penalties INT
);

-- CHAMPIONS 

CREATE TABLE champions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    season CHAR(4) NOT NULL,
    division_id INT,
    club_id INT NOT NULL
);

CREATE TABLE transfers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    year CHAR(4) NOT NULL,
    transfer_amount INT,
    gloves INT,
    player_id INT,
    club_out_id INT,
    club_in_id INT NOT NULL
);

/* CONSTRAINTS */

ALTER TABLE transfers
ADD CONSTRAINT fk_transfers_players
FOREIGN KEY(player_id)
REFERENCES players(id);

ALTER TABLE transfers
ADD CONSTRAINT fk_transfers_clubs_out
FOREIGN KEY(club_out_id)
REFERENCES clubs(id);

ALTER TABLE transfers
ADD CONSTRAINT fk_transfers_clubs_in
FOREIGN KEY(club_in_id)
REFERENCES clubs(id);

ALTER TABLE clubs
ADD CONSTRAINT fk_clubs_clubs_classes
FOREIGN KEY(club_class_id)
REFERENCES club_classes(id);

ALTER TABLE player_contracts
ADD CONSTRAINT fk_player_contracts_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE player_contracts
ADD CONSTRAINT fk_player_contracts_players
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

ALTER TABLE player_game_stats 
ADD CONSTRAINT fk_stats_players
FOREIGN KEY(player_id)
REFERENCES players(id);

ALTER TABLE stats 
ADD CONSTRAINT fk_stats_clubs
FOREIGN KEY(game_id)
REFERENCES games(id);

ALTER TABLE market_value 
ADD CONSTRAINT fk_market_value_players
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

ALTER TABLE games
ADD CONSTRAINT fk_games_competitions
FOREIGN KEY(competition_id)
REFERENCES competitions(id);

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

ALTER TABLE player_game_stats
ADD CONSTRAINT fk_player_game_stats_players
FOREIGN KEY(player_id)
REFERENCES players(id);

ALTER TABLE player_game_stats
ADD CONSTRAINT fk_players_game_stats_games
FOREIGN KEY(game_id)
REFERENCES games(id);

-- CUPS 

ALTER TABLE group_phase
ADD CONSTRAINT fk_group_phase_clubs 
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE group_phase
ADD CONSTRAINT fk_group_phase_competitions
FOREIGN KEY(competition_id)
REFERENCES competitions(id);

ALTER TABLE knock_out
ADD CONSTRAINT fk_knock_out_games
FOREIGN KEY(game_id)
REFERENCES games(id);

ALTER TABLE knock_out
ADD CONSTRAINT fk_knock_out_penalties
FOREIGN KEY(penalty_id)
REFERENCES penalties(id);


ALTER TABLE champions
ADD CONSTRAINT fk_champions_divisions
FOREIGN KEY(division_id)
REFERENCES divisions(id);

ALTER TABLE champions
ADD CONSTRAINT fk_champions_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE qualifiers
ADD CONSTRAINT fk_qualifiers_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE qualifiers
ADD CONSTRAINT fk_qualifiers_competitions
FOREIGN KEY(competition_id)
REFERENCES competitions(id);

/* add constraint unique */

ALTER TABLE coach_contracts
ADD CONSTRAINT UQ_coach_contracts_coaches
UNIQUE(coach_id);

ALTER TABLE coach_contracts
ADD CONSTRAINT UQ_coach_contracts_clubs
UNIQUE(club_id);

ALTER TABLE player_contracts
ADD CONSTRAINT UQ_player_contracts_players
UNIQUE(player_id);

ALTER TABLE champions 
ADD CONSTRAINT UQ_champion
UNIQUE(season, division_id);

ALTER TABLE competitions
ADD CONSTRAINT UQ_championship
UNIQUE(name);

ALTER TABLE championships
ADD CONSTRAINT UQ_championships_club_and_season
UNIQUE(season, division_id, club_id)

/* Keeping track from the contract updates */

CREATE TABLE backup_player_contracts(
	player_contract_id INT,
	old_start CHAR(4),
	old_end CHAR(4),
	old_transfer_amount INT,
	old_salary INT,
	old_termination_fine INT,
	old_club_id INT,
	new_start CHAR(4),
	new_end CHAR(4),
	new_transfer_amount INT,
	new_salary INT,
	new_termination_fine INT,
	new_club_id INT,
	player_id INT
);

CREATE TRIGGER update_contract 
AFTER UPDATE ON player_contracts
FOR EACH ROW 
INSERT INTO backup_player_contracts VALUES(OLD.id, OLD.start, OLD.end, OLD.transfer_amount, OLD.salary, OLD.termination_fine, OLD.club_id, NEW.start, NEW.end, NEW.transfer_amount, NEW.salary, NEW.termination_fine, NEW.club_id, OLD.player_id);

/* Usage 

UPDATE player_contracts 
SET start = 2022, end = 2024, transfer_amount = 1000000, salary = 150000, termination_fine = 4000000, club_id = 5, player_id  = 30 
where id = 1; 

*/


/* 

PLAYER SKILL 

sliding_tackle
shooting
strength
vision

short_passing
long_passing

marking

penalties

*/


/* 

CUPS TABLES 

On knock_out
match_number -> 1 or 2
ex: if single_match False
    game 1 of 2
    game 2 of 2
*/

/*

CREATE TABLE overall(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    overall INT NOT NULL,
    player_id INT
);

ALTER TABLE overall
ADD CONSTRAINT fk_overall_players
FOREIGN KEY(player_id)
REFERENCES players(id);

*/