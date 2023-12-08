UPDATE championships 
SET 	matches = matches + 1, 
		points = points + %s,
		win = win + %s, 
		draw = draw + %s, 
		loss = loss + %s, 
		goals_for = goals_for + %s, 
		goals_away = goals_away + %s
WHERE championships.club_id = %s AND championships.season = %s;
