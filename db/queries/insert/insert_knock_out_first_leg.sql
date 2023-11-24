INSERT INTO knock_out(  season, 
                        phase, 
                        single_match, 
                        match_number, 
                        home_id, 
                        away_id, 
                        home_game_stats_id, 
                        away_game_stats_id, 
                        competition_id ) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);