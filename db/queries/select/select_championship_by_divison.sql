SELECT clubs.name matches, won, draw, lost, goals_for, goals_away, goall_diff, points
FROM championships 
INNER JOIN divisions
INNER JOIN clubs
    ON (divisions.id = championships.division_id AND clubs.id = championships.club_id)
    AND (championships.season = %s AND divisions.name = %s);