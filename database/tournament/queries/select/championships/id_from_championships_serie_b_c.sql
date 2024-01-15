SELECT club_id
FROM championships
INNER JOIN divisions
    ON divisions.id = division_id
WHERE season = %s AND divisions.name IN ('Serie B','Serie C')
ORDER BY RAND() LIMIT 12;