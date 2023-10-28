CREATE DATABASE tournament_test;

USE tournament_test;

/* THIS IS AN BRUTAL EXAMPLE OF HOW THE */

CREATE TABLE player(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	positioning INT DEFAULT 0,
	reflex INT DEFAULT 0,
	diving INT DEFAULT 0,
	tackle INT DEFAULT 0,
	strength INT DEFAULT 0,
	pass INT DEFAULT 0,
	dribling INT DEFAULT 0,
	finish INT DEFAULT 0,
	penalty INT DEFAULT 0
);

INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 1', 20, 60, 60);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 2', 75, 54, 75);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 3', 90, 88, 97);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 4', 20, 15, 13);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 5', 70, 77, 83);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 6', 66, 69, 74);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 7', 89, 87, 80);
INSERT INTO player (name, positioning, reflex, diving) VALUES ('Player 8', 92, 85, 99);

SELECT	name AS 'NAME',
		positioning AS 'POSITIONING',
		reflex AS 'REFLEX',
		diving AS 'DIVING',
		CEIL((positioning + reflex + diving)/3) AS 'OVERALL' 
FROM player;


INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 9', 30, 40, 90);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 10', 50, 66, 44);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 11', 98, 95, 67);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 12', 60, 88, 65);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 13', 90, 99, 89);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 14', 77, 63, 74);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 15', 89, 80, 80);
INSERT INTO player (name, tackle, strength, pass) VALUES ('Player 16', 70, 50, 99);

SELECT	name AS 'NAME',
		tackle AS 'TACKLE',
		strength AS 'STRENGTH',
		pass AS 'PASS',
		CEIL((tackle + strength + pass)/3) AS 'OVERALL' 
FROM player;