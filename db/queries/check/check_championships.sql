SELECT championships.id 
FROM championships
INNER JOIN divisions
    ON championships.division_id = divisions.id
INNER JOIN competitions 
    ON divisions.competition_id = competitions.id
WHERE   (championships.club_id = %s 
        AND championships.season = %s 
        AND competitions.name = %s
        AND championships.matches < 38);