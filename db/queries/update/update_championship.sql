UPDATE championships 
SET matches = %s, won = %s, draw = %s, lost = %s, goals_for = %s, goals_away = %s, goall_diff = %s
WHERE (championships.club_id = %s AND championships.season = %s);