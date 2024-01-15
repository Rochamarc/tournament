CREATE DATABASE tournament_analysis;

USE tournament_analysis;

-- Player stats analysis
CREATE TABLE player_stats(
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    player_name VARCHAR(100) NOT NULL, 
    player_position CHAR(2) NOT NULL,
    season CHAR(4) NOT NULL,
    matches INT NOT NULL,
    shots INT NOT NULL,
    shots_on_target INT NOT NULL,
    goals INT NOT NULL,
    assists INT NOT NULL,
    fouls_committed INT NOT NULL,
    tackles INT NOT NULL,
    passes INT NOT NULL,
    wrong_passes INT NOT NULL,
    intercepted_passes INT NOT NULL,
    clearances INT NOT NULL,
    stolen_balls INT NOT NULL,
    clean_sheets INT NOT NULL,
    defenses INT NOT NULL,
    difficult_defenses INT NOT NULL,
    goals_conceded INT NOT NULL,  
    competition VARCHAR(100) NOT NULL,
    division VARCHAR(100),
    club_owner VARCHAR(100) NOT NULL,
    match_clubs VARCHAR(200) NOT NULL
);

-- Championships table analysis
CREATE TABLE championship_stats(
    id INT AUTO_INCREMENT PRIMARY KEY,
    club VARCHAR(100) NOT NULL,
    season CHAR(4) NOT NULL,
    competition VARCHAR(100) NOT NULL,
    division VARCHAR(100),
    matches INT,
    win INT,
    draw INT,
    loss INT,
    goals_for INT,
    goals_away INT,
    goals_diff INT,
    points INT
);

CREATE TABLE game_stats(
    id INT AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4) NOT NULL,
    competition VARCHAR(100) NOT NULL,
    confront VARCHAR(200) NOT NULL,
    home_club VARCHAR(100) NOT NULL, 
    home_goals INT NOT NULL,
    home_shots INT NOT NULL,
    home_shots_on_target INT NOT NULL,
    home_fouls INT NOT NULL,
    home_passes INT NOT NULL,
    home_wrong_passes INT NOT NULL,
    home_interceptions INT NOT NULL,
    home_tackles INT NOT NULL,
    home_stolen_balls INT NOT NULL,
    home_saves INT NOT NULL,
    home_ball_possession INT NOT NULL,
    home_offsides INT NOT NULL,
    home_freekicks INT NOT NULL,
    home_penalties INT NOT NULL,
    away_club VARCHAR(100) NOT NULL,
    away_goals INT NOT NULL,
    away_shots INT NOT NULL,
    away_shots_on_target INT NOT NULL,
    away_fouls INT NOT NULL,
    away_passes INT NOT NULL,
    away_wrong_passes INT NOT NULL,
    away_interceptions INT NOT NULL,
    away_tackles INT NOT NULL,
    away_stolen_balls INT NOT NULL,
    away_saves INT NOT NULL,
    away_ball_possession INT NOT NULL,
    away_offsides INT NOT NULL,
    away_freekicks INT NOT NULL,
    away_penalties INT NOT NULL
);