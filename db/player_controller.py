import sqlite3 
from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class PlayerData():
    @staticmethod
    def get_players(club_name) -> list:
        ''' 
        Get the players data from database by club name
        '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        val = cursor.execute("SELECT * FROM players WHERE current_club=?", (club_name, ) ).fetchall() # fetch the result

        data = val.copy()
        conn.close() # close database 

        return data

    @staticmethod
    def insert_players_db(players) -> None:
        '''
        Insert players data into the database
        '''
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()        

        for player in players:        
            player_data = player.data()
            cursor.execute(qh.open_insert_query('players'), player_data)
        
        conn.commit()
        conn.close()

        return None

    @staticmethod
    def update_player_stats(player_list) -> None:
        ''' Update players database '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        for player in player_list:
            player_data = player.get_competition_stats()
            cursor.execute(qh.open_update_query('players'), player_data)

        conn.commit()
        conn.close()

        return None

    @staticmethod 
    def update_players_age(player_list) -> None:
        ''' Update players age row from database '''
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for player in player_list:
            cursor.execute(qh.open_update_query('players_age'), [1, player.id])

        conn.commit()
        conn.close()
        return None

    @staticmethod
    def update_players_retirement(player_list: list) -> None:
        ''' Update players retirement row from database '''
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for player in player_list:
            cursor.execute(qh.open_update_query('players_retirement'), [player.retirement, player.id])

        conn.commit()
        conn.close()
        return None
    
    @staticmethod
    def get_all_players() -> list:
        ''' Get all players from database '''
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute("SELECT * FROM players").fetchall()

        data = val.copy()
        conn.close()

        return data 

    @staticmethod
    def remove_retired_playeres() -> None:
        ''' Remove players from database that are retiring '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        # remove players from database
        cursor.execute(qh.open_delete_query('retire_players'))
        
        conn.commit()
        conn.close()
        return None 
                
