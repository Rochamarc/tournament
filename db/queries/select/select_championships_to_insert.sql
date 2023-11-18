SELECT  club_id,
        division_id 
FROM championships
INNER JOIN divisions
ON divisions.id = championships.division_id AND divisions.name = %s
ORDER BY championships.points DESC;