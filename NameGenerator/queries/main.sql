USE TournamentName;

ALTER DATABASE TournamentName CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE first_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(100) NOT NULL,
    nationality VARCHAR(100)
);

CREATE TABLE last_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(100) NOT NULL,
    nationality VARCHAR(100)
);


DELIMITER $

CREATE FUNCTION GET_FULL_NAME(FIRST_NATIONALITY VARCHAR(100), LAST_NATIONALITY VARCHAR(100))
RETURNS VARCHAR(200) 
DETERMINISTIC
BEGIN
	DECLARE first_name VARCHAR(100);
	DECLARE last_name VARCHAR(100);

    SELECT first_names.value        
    FROM first_names
    WHERE first_names.nationality = FIRST_NATIONALITY 
    ORDER BY RAND() LIMIT 1
    INTO first_name;
	
    SELECT last_names.value
    FROM last_names
    WHERE last_names.nationality = LAST_NATIONALITY
    ORDER BY RAND() LIMIT 1
    INTO last_name;
   	
    RETURN CONCAT(first_name, ' ', last_name);
END;
$


DELIMITER ;