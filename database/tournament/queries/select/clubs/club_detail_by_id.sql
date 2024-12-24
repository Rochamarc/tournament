SELECT 	ch.season,
		c.name,
		d.name,
		c2.name,
		ch.points,
		ch.win,
		ch.loss,
		ch.draw,
		ch.goals_for,
		ch.goals_away 
FROM championships ch
JOIN clubs c
	ON c.id = ch.club_id
JOIN divisions d 
	ON d.id = ch.division_id
JOIN competitions c2 
	ON c2.id = d.competition_id
WHERE club_id = %s;