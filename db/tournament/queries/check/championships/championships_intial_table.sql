SELECT id 
FROM championships
WHERE   club_id = %s
        AND season = %s;