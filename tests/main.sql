/* 
	Running tests on database
*/

CREATE DATABASE tournament_test;

/* 

copying from original database 

mysqldump -u <user name> --password=<pwd> <original db> | mysql -u <user name> -p <new db>

*/


/*  
	A QUERY THAT SELECT PLAYER CONTRACTS
    AND FREE AGENTS
*/

SELECT 	pc.id,
		IFNULL(pc.start, 'NO CONTRACT') AS 'Start Contract',
		IFNULL(pc.end, 'NO CONTRACT') AS 'End Contract',
		IFNULL(pc.transfer_amount, 'FREE') AS 'Trasnfer',
		IFNULL(pc.salary, 'NO SALARY') AS 'Salary',
		IFNULL(pc.termination_fine, 'NO FINE') AS 'Fine',
		IFNULL(c.name, 'FREE AGENT') AS 'Club',
        p.id AS 'Player id',
		p.name AS 'Player',
		p.position AS 'Postion'
FROM player_contracts pc
LEFT JOIN clubs c 
	ON pc.club_id = c.id 
INNER JOIN players p 
	ON pc.player_id = p.id
ORDER BY pc.id DESC LIMIT 10;

SELECT 	pc.id,
        p.id AS 'Player id'
FROM player_contracts pc
LEFT JOIN clubs c 
	ON pc.club_id = c.id 
INNER JOIN players p 
	ON pc.player_id = p.id;

SELECT 	pc.id AS 'Player Contract id',
        p.id AS 'Player id'
FROM player_contracts pc
LEFT JOIN clubs c 
	ON pc.club_id = c.id 
INNER JOIN players p 
	ON pc.player_id = p.id
WHERE c.name IS NULL;


INSERT INTO players VALUES (NULL, 'German Cano', 'Argentina', 'CF', '1989', 1.79, 80.0, 'R');
INSERT INTO players VALUES (NULL, 'Fábio', 'Brasil', 'GK', '1980', 1.90, 80.0, 'R');
INSERT INTO players VALUES (NULL, 'Juan Mata', 'Spain', 'AM', '1987', 1.79, 79.7, 'L');
INSERT INTO players VALUES (NULL, 'Nino', 'Brasil', 'CB', '1999', 1.87, 88.0, 'R');

INSERT INTO player_contracts (player_id) VALUES (2645); 
INSERT INTO player_contracts (player_id) VALUES (2644); 
INSERT INTO player_contracts (player_id) VALUES (2643); 
INSERT INTO player_contracts (player_id) VALUES (2642); 


/* LETS ALTER SOME PLAYER_CONTRACTS.END  in 2024 and 2023 */

SELECT 	*
FROM player_contracts pc
LEFT JOIN clubs c 
	ON pc.club_id = c.id 
INNER JOIN players p 
	ON pc.player_id = p.id
WHERE pc.end = '2023';