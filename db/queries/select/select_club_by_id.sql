SELECT  clubs.id, 
        clubs.name, 
        clubs.country
FROM clubs 
WHERE clubs.id = %s;