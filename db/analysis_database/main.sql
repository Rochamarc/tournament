CREATE DATABASE football_analysis;

USE football_analysis;

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
    home VARCHAR(100) NOT NULL,
    away VARCHAR(100) NOT NULL
);

/* COPY FILES FROM MAIN DB TO ANALISYS DB */
INSERT INTO football_analysis.player_stats
SELECT  NULL,
        players.id,
        players.name,
        players.position,
        player_stats.season,
        player_stats.matches,            
        player_stats.shots,              
        player_stats.shots_on_target,    
        player_stats.goals,              
        player_stats.assists,            
        player_stats.fouls_committed,    
        player_stats.tackles,            
        player_stats.passes,             
        player_stats.wrong_passes,       
        player_stats.intercepted_passes, 
        player_stats.clearances,         
        player_stats.stolen_balls,       
        player_stats.clean_sheets,       
        player_stats.defenses,           
        player_stats.difficult_defenses, 
        player_stats.goals_conceded,
        competitions.name,
        divisions.name,
        home.name,
        away.name
FROM player_stats 
INNER JOIN players 
    ON player_stats.player_id = players.id
INNER JOIN games
    ON player_stats.game_id = games.id
INNER JOIN competitions
    ON games.competition_id = competitions.id
INNER JOIN player_contracts
    ON player_contracts.player_id = players.id
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