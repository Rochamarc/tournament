SELECT 	players.id, 
		players.name, 
		players.nationality, 
		players.birth,
		players.position, 
		players.height, 
		players.weight, 
		players.foot, 
		skills.positioning,
        skills.reflexes,
        skills.diving,
        skills.standing_tackle,
        skills.physical,
        skills.passing,
        skills.dribbling,
        skills.long_shot,
        skills.finishing, 
		clubs.id
FROM players
INNER JOIN player_contracts
INNER JOIN clubs
INNER JOIN skills
	ON skills.season = %s
	AND players.id = player_contracts.player_id 
	AND clubs.id = player_contracts.club_id
	AND players.id = skills.player_id;