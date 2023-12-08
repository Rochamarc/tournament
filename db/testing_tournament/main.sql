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

/* CUP TESTING */

/*
In this case, each table will have 4 clubs,
for example the 2023 Libertadores 

Group D

Fluminense
River Plate
Sporting Cristal
The Strongest
*/

CREATE TABLE clubs(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE competitions(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL
);

INSERT INTO clubs VALUES(NULL, 'FLUMINENSE');
INSERT INTO clubs VALUES(NULL, 'RIVER PLATE');
INSERT INTO clubs VALUES(NULL, 'SPORTING CRISTAL');
INSERT INTO clubs VALUES(NULL, 'THE STRONGEST');

INSERT INTO competitions VALUES(NULL, 'CONMEBOL LIBERTADORES DA AMERICA');

CREATE TABLE group_phase(
    id INT PRIMARY KEY AUTO_INCREMENT,
	group_name CHAR(1) NOT NULL,
    season CHAR(4) NOT NULL,
    matches INT DEFAULT 0,
    win INT DEFAULT 0,
    loss INT DEFAULT 0,
    draw INT DEFAULT 0,
    goals_for INT DEFAULT 0,
    goals_away INT DEFAULT 0,
    goals_diff INT DEFAULT 0,
    points INT DEFAULT 0,
    club_id INT,
    competition_id INT
);

ALTER TABLE group_phase
ADD CONSTRAINT fk_group_phase_clubs
FOREIGN KEY(club_id)
REFERENCES clubs(id);

ALTER TABLE group_phase
ADD CONSTRAINT fk_group_phase_competitons
FOREIGN KEY(competition_id)
REFERENCES competitions(id);

INSERT INTO group_phase(group_name, season, club_id, competition_id) VALUES ('D', '2023', 1, 1);
INSERT INTO group_phase(group_name, season, club_id, competition_id) VALUES ('D', '2023', 2, 1);
INSERT INTO group_phase(group_name, season, club_id, competition_id) VALUES ('D', '2023', 3, 1);
INSERT INTO group_phase(group_name, season, club_id, competition_id) VALUES ('D', '2023', 4, 1);

/* REAL MODEL OF PLAYER OVERALL */

CREATE TABLE player(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	position CHAR(2) NOT NULL
);


-- Position, reflex and diving only for keepers
-- Tackle, strength pass are defensive skills
-- Dribling, finishing and penalty are attacking skills

CREATE TABLE player_skill(
	id INT PRIMARY KEY AUTO_INCREMENT,
	positioning INT DEFAULT 0,
	reflex INT DEFAULT 0,
	diving INT DEFAULT 0,
	tackle INT DEFAULT 0,
	strength INT DEFAULT 0,
	passing INT DEFAULT 0,
	dribling INT DEFAULT 0,
	finish INT DEFAULT 0,
	penalty INT DEFAULT 0,
	player_id INT
);

ALTER TABLE player_skill
ADD CONSTRAINT fk_player_skill_players
FOREIGN KEY(player_id)
REFERENCES player(id);

INSERT INTO player VALUES(NULL, 'Player 1', 'GK');
INSERT INTO player VALUES(NULL, 'Player 2', 'CB');
INSERT INTO player VALUES(NULL, 'Player 3', 'AM');
INSERT INTO player VALUES(NULL, 'Player 4', 'CF');

INSERT INTO player_skill(positioning, reflex, diving, player_id) VALUES(65, 80, 82, 1);
INSERT INTO player_skill(tackle, strength, passing, dribling, finish, penalty, player_id) VALUES(70, 80, 82, 60, 55, 40, 2);
INSERT INTO player_skill(tackle, strength, passing, dribling, finish, penalty, player_id) VALUES(30, 20, 50, 80, 70, 66, 3);
INSERT INTO player_skill(tackle, strength, passing, dribling, finish, penalty, player_id) VALUES(55, 54, 55, 75, 88, 90, 4);

SELECT 	player.name,
		player.position,
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing + player_skill.dribling + player_skill.finish + player_skill.penalty)/6) AS 'Overall',
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing)/3) AS 'Defensive Overall',
		CEIL((player_skill.dribling + player_skill.finish + player_skill.penalty)/3) AS 'Attacking Overall'
FROM player
INNER JOIN player_skill
WHERE player.id = player_skill.player_id AND player.position != 'GK';

-- Ordenando por ataque
SELECT 	player.name,
		player.position,
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing + player_skill.dribling + player_skill.finish + player_skill.penalty)/6) AS 'Overall',
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing)/3) AS 'Defensive Overall',
		CEIL((player_skill.dribling + player_skill.finish + player_skill.penalty)/3) AS 'Attacking Overall'
FROM player
INNER JOIN player_skill
WHERE player.id = player_skill.player_id AND player.position != 'GK'
ORDER BY 5;

-- Ordenando por defensa
SELECT 	player.name,
		player.position,
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing + player_skill.dribling + player_skill.finish + player_skill.penalty)/6) AS 'Overall',
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing)/3) AS 'Defensive Overall',
		CEIL((player_skill.dribling + player_skill.finish + player_skill.penalty)/3) AS 'Attacking Overall'
FROM player
INNER JOIN player_skill
WHERE player.id = player_skill.player_id AND player.position != 'GK'
ORDER BY 4;

-- Ordenando por media geral
SELECT 	player.name,
		player.position,
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing + player_skill.dribling + player_skill.finish + player_skill.penalty)/6) AS 'Overall',
		CEIL((player_skill.tackle + player_skill.strength + player_skill.passing)/3) AS 'Defensive Overall',
		CEIL((player_skill.dribling + player_skill.finish + player_skill.penalty)/3) AS 'Attacking Overall'
FROM player
INNER JOIN player_skill
WHERE player.id = player_skill.player_id AND player.position != 'GK'
ORDER BY 3;


CREATE TABLE player_game_stats(
	id INT PRIMARY KEY AUTO_INCREMENT,
	assists INT DEFAULT 0,
	goals INT DEFAULT 0,
	tackles INT DEFAULT 0,
	defenses INT DEFAULT 0,
	passes INT DEFAULT 0,
	wrong_passes INT DEFAULT 0,
	intercepted_passes INT DEFAULT 0,
	dificult_defenses INT DEFAULT 0,
	clearances INT DEFAULT 0,
	fouls INT DEFAULT 0,
	stolen_balls INT DEFAULT 0,
	player_id INT,
	game_id INT	
);

/*
player_id FOREIGN KEY
game_id FOREIGN KEY
*/
