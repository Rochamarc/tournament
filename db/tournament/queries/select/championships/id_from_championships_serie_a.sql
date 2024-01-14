SELECT  championships.club_id
FROM championships
INNER JOIN divisions
    ON divisions.id = division_id
WHERE season = %s AND divisions.name = 'Serie A';