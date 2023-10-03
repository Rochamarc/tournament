SELECT clubs.id, clubs.name, clubs.country, divisions.name  
FROM clubs 
INNER JOIN championships 
INNER JOIN divisions 
    ON division_id=divisions.id 
    AND clubs.id = championships.club_id
    AND divisions.name = 'Serie B';