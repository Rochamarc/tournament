SELECT divisions.id, divisions.name, competitions.name 
FROM divisions 
INNER JOIN competitions 
    ON competition_id=competitions.id;
