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