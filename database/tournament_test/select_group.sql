SELECT  competitions.name,
        clubs.name,
        group_phase.matches,
        group_phase.win,
        group_phase.loss,
        group_phase.draw,
        group_phase.goals_for,
        group_phase.points 
FROM group_phase
INNER JOIN clubs
INNER JOIN competitions
    ON club_id = clubs.id AND competition_id = competitions.id;