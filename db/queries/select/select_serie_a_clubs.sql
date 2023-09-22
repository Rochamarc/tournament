SELECT clubs.id, clubs.name, clubs.country, divisons.name  
FROM clubs 
INNER JOIN championships 
INNER JOIN divisons 
    ON divison_id=divisons.id 
    AND clubs.id = championships.club_id
    AND divisons.name = 'Serie A';