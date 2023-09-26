SELECT players.id, players.name, players.nationality, players.birth,
players.position, players.height, players.weight, players.foot, overall.overall, clubs.id
FROM players
INNER JOIN player_contracts
INNER JOIN clubs
INNER JOIN overall 
	ON overall.season = %s
	AND players.id = player_contracts.player_id 
	AND clubs.id = player_contracts.club_id
	AND players.id = overall.player_id;