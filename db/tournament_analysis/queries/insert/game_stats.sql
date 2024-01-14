USE tournament;

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