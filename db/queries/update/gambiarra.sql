/* this query is to fix a bug in stats of some players */

UPDATE stats SET matches = 1
WHERE 	matches = 0 AND 
		(shots OR 
		shots_on_target OR
		goals OR
		assists OR
		fouls_committed OR
		tackles OR
		passes OR
		wrong_passes OR
		intercepted_passes OR
		clearances OR
		stolen_balls OR
		clean_sheets OR
		defenses OR
		difficult_defenses OR
		goals_conceded) > 0; 