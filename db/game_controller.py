import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class GameData():
    @staticmethod
    def insert_game_db(game) -> None:
        ''' Insert one game into the database '''
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        try:
            game_data = game.game_data()
        except:
            game_data = game 
        
        cursor.execute(qh.open_insert_query('games'), game_data)

        conn.commit()
        conn.close()
        
        return None    

    @staticmethod
    def insert_games_db(game_list: list) -> None:
        ''' 
            Insert game data into database 

            below the order to receive the data 
            [ competition, season, hour, home_team, away_team, score, stadium, home_shots, home_shots_on_target, home_fouls, 
            home_tackles, home_saves, home_ball_possession, home_offsides, home_freekicks, away_shots, away_shots_on_target,
            away_fouls, away_tackles, away_saves, away_ball_possession, away_offsides, away_freekicks ]
        '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for game in game_list:
            game_data = game.game_data()

            cursor.execute(qh.open_insert_query('games'), game_data)

        conn.commit()
        conn.close()

        return None    