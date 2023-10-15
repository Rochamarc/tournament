SELECT clubs.id, clubs.name, clubs.country, championships.division  
FROM clubs 
INNER JOIN championships  
    ON clubs.id = championships.club_id
WHERE championships.division = 'Serie B';