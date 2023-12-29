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


USE tournament; 

-- COPY FILES FROM MAIN DB TO ANALISYS DB 
INSERT INTO tournament_analysis.player_stats
SELECT  NULL,
        players.id AS 'player_id',
        players.name,
        players.position,
        stats.season,
        stats.matches,            
        stats.shots,              
        stats.shots_on_target,    
        stats.goals,              
        stats.assists,            
        stats.fouls_committed,    
        stats.tackles,            
        stats.passes,             
        stats.wrong_passes,       
        stats.intercepted_passes, 
        stats.clearances,         
        stats.stolen_balls,       
        stats.clean_sheets,       
        stats.defenses,           
        stats.difficult_defenses, 
        stats.goals_conceded,
        competitions.name AS 'competition',
        divisions.name AS 'division',
        club_owner.name AS 'club_owner',
        CONCAT(home.name,' x ',away.name) AS 'match' 
FROM stats 
INNER JOIN players 
    ON stats.player_id = players.id
INNER JOIN games
    ON stats.game_id = games.id
INNER JOIN competitions
    ON games.competition_id = competitions.id
INNER JOIN player_contracts
    ON player_contracts.player_id = players.id
INNER JOIN clubs club_owner
    ON player_contracts.club_id = club_owner.id
INNER JOIN game_stats home_game_stats
    ON games.home_game_stats_id = home_game_stats.id
INNER JOIN game_stats away_game_stats
    ON games.away_game_stats_id = away_game_stats.id
INNER JOIN clubs home
    ON home_game_stats.club_id = home.id
INNER JOIN clubs away
    ON away_game_stats.club_id = away.id
INNER JOIN championships
    ON home.id = championships.club_id
INNER JOIN divisions
    ON divisions.id = championships.division_id
ORDER BY players.id;

-- Insert values from tournament table
INSERT INTO tournament_analysis.championship_stats
SELECT  NULL,
        clubs.name,
        championships.season,
        competitions.name,
        divisions.name,
        championships.matches, 
        championships.win, 
        championships.draw, 
        championships.loss, 
        championships.goals_for, 
        championships.goals_away, 
        championships.goals_diff, 
        championships.points
FROM championships 
INNER JOIN clubs
    ON (clubs.id = championships.club_id)
INNER JOIN divisions
    ON (divisions.id = championships.division_id)
INNER JOIN competitions
    ON (competitions.id = divisions.competition_id);

INSERT INTO tournament_analysis.game_stats
SELECT	NULL,
        g.season,
		c.name,
		CONCAT(home_club.name, ' x ', away_club.name),
		home_club.name,
		home_stats.goals,
        home_stats.shots,
        home_stats.shots_on_target,
        home_stats.fouls,
        home_stats.passes,
        home_stats.wrong_passes,
        home_stats.interceptions,
        home_stats.tackles,
        home_stats.stolen_balls,
        home_stats.saves,
        home_stats.ball_possession,
        home_stats.offsides,
        home_stats.freekicks,
        home_stats.penalties,
		away_club.name,
        away_stats.goals,
        away_stats.shots,
        away_stats.shots_on_target,
        away_stats.fouls,
        away_stats.passes,
        away_stats.wrong_passes,
        away_stats.interceptions,
        away_stats.tackles,
        away_stats.stolen_balls,
        away_stats.saves,
        away_stats.ball_possession,
        away_stats.offsides,
        away_stats.freekicks,
        away_stats.penalties
FROM games g
INNER JOIN game_stats home_stats
	ON home_stats.id = g.home_game_stats_id 
INNER JOIN game_stats away_stats
	ON away_stats.id = g.away_game_stats_id
INNER JOIN clubs home_club
	ON home_club.id = home_stats.club_id
INNER JOIN clubs away_club
	ON away_club.id = away_stats.club_id
INNER JOIN competitions c
	ON g.competition_id = c.id;