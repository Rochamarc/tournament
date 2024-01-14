SELECT  p.id AS "player id",
		cc.name AS "club class",
		p.position
FROM player_contracts pc 
INNER JOIN clubs cl 
	ON pc.club_id = cl.id
INNER JOIN players p 
	ON pc.player_id = p.id
INNER JOIN club_classes cc 
	ON cl.club_class_id = cc.id;