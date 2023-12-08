SELECT  clubs.id, 
        clubs.name, 
        clubs.country, 
        divisions.name  
FROM clubs 
INNER JOIN championships  
INNER JOIN divisions 
    ON clubs.id = championships.club_id
    AND championships.division_id = divisions.id
WHERE divisions.name = 'Serie C' AND championships.season = %s;