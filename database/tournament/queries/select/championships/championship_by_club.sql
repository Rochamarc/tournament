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
JOIN clubs
	ON (championships.club_id = clubs.id)
WHERE championships.season = %s AND clubs.id = %s;