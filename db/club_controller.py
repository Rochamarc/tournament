import sqlite3 
import mysql.connector

from db.open_query import QueryHelper
from db.database import export_database_config

database = 'db/database.db'

qh = QueryHelper()


class ClubData():
    @staticmethod
    def insert_clubs_db(clubs: list) -> None:
        '''
        Insert clubs into the database
        '''
        conn = mysql.connector.connect(**export_database_config())
        cursor = conn.cursor()
         
        for club in clubs:
            club_data = club.data() 
            cursor.execute(qh.open_insert_query('clubs'), club_data)
        
        conn.commit()
        conn.close()

        return None

    @staticmethod
    def get_clubs(clubs: list) -> list:
        ''' Get clubs info from database '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        data = []

        for club in clubs:
            val = cursor.execute("SELECT * FROM clubs WHERE name=?", (club, )).fetchall() 
            data.append(val.copy())

        conn.close()

        return data

    @staticmethod
    def get_clubs_by_country(country) -> list:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
    
        val = cursor.execute("SELECT * FROM clubs WHERE country=?", (country, )).fetchall()
        data = val.copy()

        conn.close()
        return data 