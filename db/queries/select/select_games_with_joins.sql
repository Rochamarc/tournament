SELECT 	games.id,
		games.season,
		games.weather,
		games.hour,
		games.stadium,
		games.audience,
		home_club.name AS 'home',
		away_club.name AS 'away',
		home.goals AS 'home.goals',           
		home.shots AS 'home.shots',           
		home.shots_on_target AS 'home.shots_on_target', 
		home.fouls AS 'home.fouls',           
		home.tackles AS 'home.tackles',         
		home.stolen_balls AS 'home.stolen_balls',    
		home.saves AS 'home.saves',           
		home.ball_possession AS 'home.ball_possession', 
		home.offsides AS 'home.offsides',        
		home.freekicks AS 'home.freekicks',       
		home.penalties AS 'home.penalties',             
		away.goals AS 'away.goals',           
		away.shots AS 'away.shots',           
		away.shots_on_target AS 'away.shots_on_target', 
		away.fouls AS 'away.fouls',           
		away.tackles AS 'away.tackles',         
		away.stolen_balls AS 'away.stolen_balls',    
		away.saves AS 'away.saves',           
		away.ball_possession AS 'away.ball_possession', 
		away.offsides AS 'away.offsides',        
		away.freekicks AS 'away.freekicks',       
		away.penalties AS 'away.penalties'
FROM games
INNER JOIN game_stats home
INNER JOIN game_stats away
INNER JOIN clubs home_club
INNER JOIN clubs away_club
	ON (home.id = home_game_stats_id 
	AND away.id = away_game_stats_id)
	AND (home_club.id = home.club_id
	AND away_club.id = away.club_id);