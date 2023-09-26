SELECT matches, won, draw, lost, goals_for, goals_away, goall_diff 
FROM championships 
WHERE (club_id = %s AND season = %s);