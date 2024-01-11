SELECT 	pc.id AS 'Player Contract id',
        p.id AS 'Player id'
FROM player_contracts pc
LEFT JOIN clubs c 
	ON pc.club_id = c.id 
INNER JOIN players p 
	ON pc.player_id = p.id
WHERE c.name IS NULL;