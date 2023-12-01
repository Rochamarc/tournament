SELECT  players.id AS 'player_id',
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
        competitions.name AS 'competition',
        divisions.name AS 'division',
        club_owner.name AS 'club_owner',
        CONCAT(home.name,' x ',away.name) AS 'match' 
FROM player_stats 
INNER JOIN players 
    ON player_stats.player_id = players.id
INNER JOIN games
    ON player_stats.game_id = games.id
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

/* Subquerie */
SELECT  games.season,
        games.hour,
        games.climate,
        games.weather,
        home.name,
        away.name
FROM games 
INNER JOIN game_stats home_stats
    ON games.home_game_stats_id = home_stats.id
INNER JOIN game_stats away_stats
    ON games.away_game_stats_id = away_stats.id
INNER JOIN clubs home
    ON home_stats.club_id = home.id
INNER JOIN clubs away
    ON away_stats.club_id = away.id;


