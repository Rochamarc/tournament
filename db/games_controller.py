from db.base_controller import BaseController
import mysql.connector 

class GamesController(BaseController):
    @classmethod
    def insert_games_list(cls, games_data: list) -> None:
        ''' Insert a list of games into the database '''
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for game_data in games_data:
            cursor.execute(cls.get_insert_query('insert_game'), game_data)

        conn.commit()
        conn.close()

    @classmethod
    def insert_game_stat_with_id_return(cls, game_data: list) -> None:
        ''' Insert game stats and return his id '''

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_insert_query('insert_game_stats'), game_data)
        conn.commit()

        conn.close()
        return cls.select_last_id()
    
    @classmethod
    def select_last_id(cls) -> list:
        ''' Select the last game_stats.id that was inserted '''

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_game_stats_id_last_inserted'))
        id = cursor.fetchall()
        
        conn.close()
        return id 