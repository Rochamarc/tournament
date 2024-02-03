/* ADD TRIGGERS */

DELIMITER $

CREATE TRIGGER rtr_players 
BEFORE DELETE ON players 
FOR EACH ROW
BEGIN 
    INSERT INTO retired_players VALUES(NULL, OLD.id, OLD.name, OLD.nationality, OLD.position, OLD.birth, OLD.foot);
END
$

CREATE TRIGGER update_goals_diff
BEFORE UPDATE ON championships
FOR EACH ROW
BEGIN
    SET NEW.goals_diff = NEW.goals_for - NEW.goals_away;
END
$

CREATE PROCEDURE GET_PLAYER_OVERALL(PLAYER_ID INT, PLAYER_POSITION CHAR(2), SEASON CHAR(4))
BEGIN 
    CASE 
        WHEN PLAYER_POSITION = 'GK' THEN SELECT ROUND((positioning + reflexes + diving) / 3, 0) 
            FROM skills where (skills.player_id = PLAYER_ID AND skills.season = SEASON);
        WHEN PLAYER_POSITION != 'GK' THEN SELECT ROUND((standing_tackle + physical + passing + dribbling + long_shot + finishing) / 6, 0) 
            FROM skills WHERE (skills.player_id = PLAYER_ID AND skills.season = SEASON);
    END CASE;
END
$

/*
CREATE FUNCTION GET_PLAYER_OVERALL(PLAYER_ID INT, PLAYER_POSITION VARCHAR(4), SEASON VARCHAR(6)) RETURNS INTEGER DETERMINISTIC
    RETURN CASE PLAYER_POSITION
        WHEN PLAYER_POSITION = 'GK' THEN (SELECT ROUND((positioning + reflexes + diving) / 3, 0) FROM skills WHERE (skills.player_id = PLAYER_ID AND skills.season = SEASON))
        WHEN PLAYER_POSITION != 'GK' THEN (SELECT ROUND((standing_tackle + physical + passing + dribbling + long_shot + finishing) / 6, 0) FROM skills WHERE (skills.player_id = PLAYER_ID AND skills.season = SEASON))
    END;
$

--READS SQL DATA DETERMINISTIC;  

*/


CREATE FUNCTION GET_PLAYER_OVERALL(PLAYER_ID INT, `PLAYER_POSITION` CHAR(2), SEASON CHAR(4))
RETURNS INT DETERMINISTIC

BEGIN 
    DECLARE overall INT;

    IF `PLAYER_POSITION` = 'GK' THEN
        SELECT ROUND((positioning + reflexes + diving) / 3, 0) FROM skills WHERE (skills.player_id = PLAYER_ID AND skills.season = SEASON) INTO overall;
    ELSE 
        SELECT ROUND((standing_tackle + physical + passing + dribbling + long_shot + finishing) / 6, 0) FROM skills WHERE (skills.player_id = PLAYER_ID AND skills.season = SEASON) INTO overall;
    END IF;

    RETURN (overall);
    
END;
$

CREATE FUNCTION GET_PLAYER_AGE(PLAYER_BIRTH CHAR(4), SEASON INT)
RETURNS INT DETERMINISTIC

BEGIN 
    DECLARE age INT;

    SET age = (SEASON - (PLAYER_BIRTH * 1));

    RETURN(age);
END;
$

CREATE PROCEDURE GET_PLAYERS_BY_OVERALL(SEASON_SEARCH CHAR(4), OVERALL_SEARCH INT)
BEGIN
    SELECT  pl.id,
            pl.name,
            pl.nationality,
            pl.position,
            GET_PLAYER_AGE(pl.birth, SEASON_SEARCH) AS 'age',
            pl.height,
            pl.foot,
            GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) AS 'overall',
            FORMAT(mk.value, 2) AS 'market value',
            FORMAT(pc.salary, 2) AS 'salary',
            cl_owner.name AS 'club owner'
    FROM players pl
    INNER JOIN skills sk
        ON pl.id = sk.player_id AND sk.season = SEASON_SEARCH
    INNER JOIN market_value mk
        ON pl.id = mk.player_id AND mk.season = SEASON_SEARCH
    INNER JOIN player_contracts pc
        ON pl.id = pc.player_id
    INNER JOIN clubs cl_owner
        ON pc.club_id = cl_owner.id
    WHERE GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) >= OVERALL_SEARCH
    ORDER BY GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) DESC;
END;
$

CREATE PROCEDURE GET_PLAYERS_BY_POSITION(SEASON_SEARCH CHAR(4), POSITION_SEARCH CHAR(2))
BEGIN 
   SELECT   pl.id,
            pl.name,
            pl.nationality,
            pl.position,
            GET_PLAYER_AGE(pl.birth, SEASON_SEARCH) AS 'age',
            pl.height,
            pl.foot,
            GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) AS 'overall',
            FORMAT(mk.value, 2) AS 'market value',
            FORMAT(pc.salary, 2) AS 'salary',
            cl_owner.name AS 'club owner'
    FROM players pl
    INNER JOIN skills sk
        ON pl.id = sk.player_id AND sk.season = SEASON_SEARCH
    INNER JOIN market_value mk
        ON pl.id = mk.player_id AND mk.season = SEASON_SEARCH
    INNER JOIN player_contracts pc
        ON pl.id = pc.player_id
    INNER JOIN clubs cl_owner
        ON pc.club_id = cl_owner.id
    WHERE pl.position = POSITION_SEARCH
    ORDER BY GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) DESC;
END;
$

CREATE PROCEDURE GET_PLAYERS_BY_AGE(SEASON_SEARCH CHAR(4), AGE_SEARCH INT)
BEGIN 
   SELECT   pl.id,
            pl.name,
            pl.nationality,
            pl.position,
            GET_PLAYER_AGE(pl.birth, SEASON_SEARCH) AS 'age',
            pl.height,
            pl.foot,
            GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) AS 'overall',
            FORMAT(mk.value, 2) AS 'market value',
            FORMAT(pc.salary, 2) AS 'salary',
            cl_owner.name AS 'club owner'
    FROM players pl
    INNER JOIN skills sk
        ON pl.id = sk.player_id AND sk.season = SEASON_SEARCH
    INNER JOIN market_value mk
        ON pl.id = mk.player_id AND mk.season = SEASON_SEARCH
    INNER JOIN player_contracts pc
        ON pl.id = pc.player_id
    INNER JOIN clubs cl_owner
        ON pc.club_id = cl_owner.id
    WHERE GET_PLAYER_AGE(pl.birth, SEASON_SEARCH) = AGE_SEARCH
    ORDER BY GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) DESC;
END;
$


CREATE PROCEDURE GET_PLAYERS_BY_ALL(SEASON_SEARCH CHAR(4), OVERALL_SEARCH INT, POSITION_SEARCH CHAR(2))
BEGIN 
   SELECT   pl.id,
            pl.name,
            pl.nationality,
            pl.position,
            GET_PLAYER_AGE(pl.birth, SEASON_SEARCH) AS 'age',
            pl.height,
            pl.foot,
            GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) AS 'overall',
            FORMAT(mk.value, 2) AS 'market value',
            FORMAT(pc.salary, 2) AS 'salary',
            cl_owner.name AS 'club owner'
    FROM players pl
    INNER JOIN skills sk
        ON pl.id = sk.player_id AND sk.season = SEASON_SEARCH
    INNER JOIN market_value mk
        ON pl.id = mk.player_id AND mk.season = SEASON_SEARCH
    INNER JOIN player_contracts pc
        ON pl.id = pc.player_id
    INNER JOIN clubs cl_owner
        ON pc.club_id = cl_owner.id
    WHERE (GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) >= OVERALL_SEARCH 
        AND pl.position = POSITION_SEARCH)
    ORDER BY GET_PLAYER_OVERALL(pl.id, pl.position, SEASON_SEARCH) ASC;
END;
$

-- POSSO COLOCAR ESSA CLAUSULA DE OVERALL COMO MAIOR OU IGUAL

DELIMITER ;