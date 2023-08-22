SELECT players.id, players.name, players.nationality, players.birth_year, players.position, 
players.height, players.weight, players.foot, players_overall.overall
FROM players
INNER JOIN players_overall
	ON players.id = players_overall.id_player;