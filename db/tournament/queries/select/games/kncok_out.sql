SELECT  competitions.name,
        knock_out.season,
        knock_out.phase,
        knock_out.match_number,
        home.name AS home,
        home_stats.goals home_goals,
        away.name AS away,
        away_stats.goals away_goals
FROM knock_out
INNER JOIN clubs home
    ON knock_out.home_id = home.id
INNER JOIN clubs away
    ON knock_out.away_id = away.id
INNER JOIN competitions
    ON knock_out.competition_id = competitions.id
INNER JOIN game_stats home_stats
    ON knock_out.home_game_stats_id = home_stats.id
INNER JOIN game_stats away_stats
    ON knock_out.away_game_stats_id = away_stats.id;