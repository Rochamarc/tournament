SELECT players.id, players.name, players.nationality, players.position,
players.birth, players.height, players.weight, players.foot, clubs.id
FROM players
INNER JOIN player_contracts 
INNER JOIN clubs 
    ON clubs.name = %s
    AND (clubs.id = player_contracts.club_id 
    AND players.id = player_contracts.player_id);