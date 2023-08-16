import mysql.connector

from db.open_query import QueryHelper
from db.database import export_database_config

database = 'db/database.db'

qh = QueryHelper()

class DomesticLeague():
    @staticmethod
    def create_domestic_table(division: str, season: str) -> None:
        ''' Create domestic table '''
        # conn = mysql.connector.connect(**export_database_config())*export_database_config())
        conn = mysql.connector.connect(**export_database_config())
        cursor = conn.cursor()

        division.replace(' ', '_')
        
        cursor.execute(qh.open_create_query('brasileirao').format(division, season))

        conn.close() # close database

        return None
    
    @staticmethod
    def domestic_table_basic(club_names: list, division: str, season: str) -> None:
        '''
        Insert club domestic cup data into the database
        '''

        division.replace(' ', '_')

        conn = mysql.connector.connect(**export_database_config())
        cursor = conn.cursor()

        for club in club_names:   
            ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]

            cursor.execute(qh.open_insert_query('brasileirao').format(division, season), ls)
        
        conn.commit()
        conn.close()

        return None

    @staticmethod
    def update_domestic_table(club_stats: list, division: str, season: str) -> None:
        ''' Update values from domestic table '''
        conn = mysql.connector.connect(**export_database_config())
        cursor = conn.cursor()

        division.replace(' ', '_')

        cursor.execute(qh.open_update_query('brasileirao').format(division, season), club_stats)
        
        conn.commit()
        conn.close()
        
        return None

    @staticmethod
    def get_domestic_cup_table(division: str, season:str) -> list:
        ''' Get the domestic cup table data '''
        conn = mysql.connector.connect(**export_database_config())
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM campeonato_brasileiro_{division}_{season}")
        
        data = cursor.fetchall() # create a copy of the fetch data
        conn.close()
        
        return data
