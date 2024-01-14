/* this select all data */

SELECT	g.season,
		c.name AS 'competition',
		CONCAT(home_club.name, ' x ', away_club.name) AS 'confront',
		home_club.name AS 'home_club',
		home_stats.goals AS 'home_goals',
        home_stats.shots AS 'home_shots',
        home_stats.shots_on_target AS 'home_shots_on_target',
        home_stats.fouls AS 'home_fouls',
        home_stats.passes AS 'home_passes',
        home_stats.wrong_passes AS 'home_wrong_passes',
        home_stats.interceptions AS 'home_interceptions',
        home_stats.tackles AS 'home_tackles',
        home_stats.stolen_balls AS 'home_stolen_balls',
        home_stats.saves AS 'home_saves',
        home_stats.ball_possession AS 'home_ball_possession',
        home_stats.offsides AS 'home_offsides',
        home_stats.freekicks AS 'home_freekicks',
        home_stats.penalties AS 'home_penalties',
		away_club.name AS 'away_club',
        away_stats.goals AS 'away_goals',
        away_stats.shots AS 'away_shots',
        away_stats.shots_on_target AS 'away_shots_on_target',
        away_stats.fouls AS 'away_fouls',
        away_stats.passes AS 'away_passes',
        away_stats.wrong_passes AS 'away_wrong_passes',
        away_stats.interceptions AS 'away_interceptions',
        away_stats.tackles AS 'away_tackles',
        away_stats.stolen_balls AS 'away_stolen_balls',
        away_stats.saves AS 'away_saves',
        away_stats.ball_possession AS 'away_ball_possession',
        away_stats.offsides AS 'away_offsides',
        away_stats.freekicks AS 'away_freekicks',
        away_stats.penalties AS 'away_penalties'
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



/* this shows all away data */

SELECT	g.season,
		c.name AS 'competition',
		CONCAT(home_club.name, ' x ', away_club.name) AS 'confront',
		away_club.name AS 'club',
		away_stats.goals AS 'goals',
        away_stats.shots AS 'shots',
        away_stats.shots_on_target AS 'shots_on_target',
        away_stats.fouls AS 'fouls',
        away_stats.passes AS 'passes',
        away_stats.wrong_passes AS 'wrong_passes',
        away_stats.interceptions AS 'interceptions',
        away_stats.tackles AS 'tackles',
        away_stats.stolen_balls AS 'stolen_balls',
        away_stats.saves AS 'saves',
        away_stats.ball_possession AS 'ball_possession',
        away_stats.offsides AS 'offsides',
        away_stats.freekicks AS 'freekicks',
        away_stats.penalties AS 'penalties'
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

/* this shows all home data */

SELECT	g.season,
		c.name AS 'competition',
		CONCAT(home_club.name, ' x ', away_club.name) AS 'confront',
		home_club.name AS 'club',
		home_stats.goals AS 'goals',
        home_stats.shots AS 'shots',
        home_stats.shots_on_target AS 'shots_on_target',
        home_stats.fouls AS 'fouls',
        home_stats.passes AS 'passes',
        home_stats.wrong_passes AS 'wrong_passes',
        home_stats.interceptions AS 'interceptions',
        home_stats.tackles AS 'tackles',
        home_stats.stolen_balls AS 'stolen_balls',
        home_stats.saves AS 'saves',
        home_stats.ball_possession AS 'ball_possession',
        home_stats.offsides AS 'offsides',
        home_stats.freekicks AS 'freekicks',
        home_stats.penalties AS 'penalties'
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