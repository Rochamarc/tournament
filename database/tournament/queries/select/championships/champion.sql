SELECT 	championships.season,
		championships.division_id,
		championships.club_id
FROM championships 
INNER JOIN divisions 
    ON championships.division_id = divisions.id
WHERE (championships.season = %s AND divisions.name = %s)
ORDER BY championships.points DESC 
LIMIT 1; 