SELECT divisons.id, divisons.name, competitions.name 
FROM divisons 
INNER JOIN competitions 
    ON competition_id=competitions.id;
