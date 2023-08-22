SELECT players.id, players.name, players.nationality, players.birth_year, players.position, 
players.height, players.weight, players.foot, players_overall.overall, clubs.name
FROM players
INNER JOIN players_overall 
INNER JOIN players_contract
INNER JOIN clubs
	ON players.id = players_overall.id_player 
	AND players.id = players_contract.id_player 
	AND clubs.id = players_contract.id_club
WHERE clubs.name = %s;