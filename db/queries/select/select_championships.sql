SELECT 	clubs.name,
		championships.matches, 
		championships.win, 
		championships.draw, 
		championships.loss, 
		championships.goals_for, 
		championships.goals_away, 
		championships.goals_diff, 
		championships.points
FROM championships 
INNER JOIN clubs
	ON (championships.club_id = clubs.id)
INNER JOIN divisions
	ON (championships.division_id = divisions.id )
WHERE championships.season = '2022' and divisions.name = 'Serie A'
ORDER BY championships.points DESC;