SELECT clubs.name matches, won, draw, lost, goals_for, goals_away, goall_diff, points
FROM championships 
INNER JOIN clubs
    ON (clubs.id = championships.club_id)
    AND (championships.season = %s AND championships.division = %s);