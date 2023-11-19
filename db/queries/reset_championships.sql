-- Zera a tabela

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

-- Remove os clubs da tabela
DELETE FROM championships WHERE season = '2023';