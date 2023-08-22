SELECT clubs.id, clubs.name, clubs.country, clubs.class, confederations.name 
FROM clubs 
INNER JOIN confederations 
    ON confederations.id = clubs.id_confederation 
WHERE clubs.country = %s;