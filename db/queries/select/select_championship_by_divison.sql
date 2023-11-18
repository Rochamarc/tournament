SELECT  clubs.name, 
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
WHERE (championships.season = %s AND divisions.name = %s)
ORDER BY championships.points DESC;