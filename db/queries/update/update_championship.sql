UPDATE championships 
SET 	matches = matches + 1, 
		win = %s, 
		draw = %s, 
		loss = %s, 
		goals_for = %s, 
		goals_away = %s, 
		goals_diff = %s
WHERE 	(championships.club_id = %s 
	AND championships.season = %s);