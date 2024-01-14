SELECT  positioning,
        reflexes,
        diving,
        standing_tackle,
        physical,
        passing,
        dribbling,
        long_shot,
        finishing,
        player_id
FROM skills
WHERE season = %s
ORDER BY(player_id) DESC LIMIT 30;