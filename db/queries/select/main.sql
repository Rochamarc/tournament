SELECT divisions.id, divisions.name, competitions.name 
FROM divisions 
INNER JOIN competitions 
    ON competition_id=competitions.id;

/* select a division table */

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
	ON championships.club_id = clubs.id
INNER JOIN divisions 
    ON championships.division_id = divisions.id
WHERE (championships.season = '2022' AND divisions.name = 'Serie A'); 

/* ordering */
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
	ON championships.club_id = clubs.id
INNER JOIN divisions 
    ON championships.division_id = divisions.id
WHERE (championships.season = '2022' AND divisions.name = 'Serie A')
ORDER BY championships.points DESC; 