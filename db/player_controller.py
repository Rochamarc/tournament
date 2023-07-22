import sqlite3 
from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class PlayerData():
    @staticmethod
    def get_players(club_name) -> list:
        ''' 
        Get the players info from database
        '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        val = cursor.execute("SELECT * FROM players WHERE current_club=?", (club_name, ) ).fetchall() # fetch the result

        data = val.copy()
        conn.close() # close database 

        return data

    @staticmethod
    def insert_players_db(players, verbose=False) -> bool:
        '''
        Insert players data into the database
        '''

        if verbose: print("Inserting players on the database")
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()        

        
        for player in players:        
            if verbose : print(f"Insert player {player} into the database")
            player_data = player.data()
            cursor.execute(qh.open_insert_query('players'), player_data)
        
        conn.commit()
        conn.close()

        if verbose : print("Players inserted into the database sucessfully!")

        return True

    @staticmethod
    def update_player_stats(player_list, verbose=False):
        ''' Update players database '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        for player in player_list:
            # print('.', sep=' ', end=' ', flush=True)
            
            player_data = player.get_competition_stats()

            if verbose : print(f"Update {player}")

            cursor.execute(qh.open_update_query('players'), player_data)

        conn.commit()
        conn.close()

        if verbose : print("Player updated sucessfully!")
        return True

    @staticmethod 
    def update_players_age(player_list, verbose=False):
        ''' Update players age '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for player in player_list:
            if verbose: print(f"Update: {player}")

            cursor.execute(qh.open_update_query('players_age'), [1, player.id])

        conn.commit()
        conn.close()
        return True