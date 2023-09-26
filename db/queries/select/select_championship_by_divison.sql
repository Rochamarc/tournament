SELECT clubs.name matches, won, draw, lost, goals_for, goals_away, goall_diff, points
FROM championships 
INNER JOIN divisons
INNER JOIN clubs
    ON (divisons.id = championships.divison_id AND clubs.id = championships.club_id)
    AND (championships.season = %s AND divisons.name = %s);