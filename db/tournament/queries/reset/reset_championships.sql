-- remove all championships tables that are not 2022 season
DELETE FROM championships WHERE season != '2022';

-- DELETING FROM SCRATCH 
DELETE FROM stats;
DELETE FROM games;
DELETE FROM game_stats;
DELETE FROM champions;

-- Makes the original tables zeros
UPDATE championships SET
    matches = 0,
    win = 0,
    loss = 0,
    draw = 0,
    goals_for = 0,
    goals_away = 0,
    goals_diff = 0,
    points = 0
WHERE season = '2022';
