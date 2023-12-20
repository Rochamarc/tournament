SELECT  champions.id
FROM champions
INNER JOIN divisions
    ON champions.division_id = divisions.id 
INNER JOIN competitions
    ON divisions.competition_id = competitions.id
WHERE competitions.name = %s AND divisions.name = %s AND champions.season = %s;


/* example */
/*
SELECT  champions.id
FROM champions
INNER JOIN divisions
    ON champions.division_id = divisions.id 
INNER JOIN competitions
    ON divisions.competition_id = competitions.id
WHERE competitions.name = 'Campeonato Brasileiro' AND divisions.name = 'Serie A' AND champions.season = '2022';
*/