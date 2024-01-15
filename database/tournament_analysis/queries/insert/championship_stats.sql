USE tournament;

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