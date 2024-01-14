SELECT * FROM stadium_ownership 
INNER JOIN clubs 
INNER JOIN stadiums 
    ON clubs.id = stadium_ownership.club_id AND stadiums.id = stadium_ownership.stadium_id;