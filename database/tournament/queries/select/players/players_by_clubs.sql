SELECT  p.name,
		p.nationality,
		p.`position`,
		p.birth,
		p.height,
		p.weight,
		p.foot,
		pc.salary,
		s.positioning,
		s.reflexes,
		s.diving,
		s.standing_tackle,
		s.physical,
		s.passing,
		s.dribbling,
		s.long_shot,
		s.finishing,
		clubs.name
	FROM players p 
	JOIN player_contracts pc 
		ON p.id = pc.player_id 
	INNER JOIN clubs 
		ON clubs.id = pc.club_id
	INNER JOIN skills s 
		ON s.player_id = p.id 
WHERE clubs.name = %s;