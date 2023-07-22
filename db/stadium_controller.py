import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class StadiumData():
    @staticmethod
    def insert_stadiums_db(stadiums: list) -> None:
        ''' Insert stadiums to the database '''
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        for stadium in stadiums:
            std_data = stadium.data

            cursor.execute(qh.open_insert_query('stadiums'), std_data)

        conn.commit()
        conn.close()

        return None

    @staticmethod
    def get_stadiums() -> list:
        ''' Get stadiums data '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute("SELECT * FROM stadium").fetchall()

        data = val.copy()
        conn.close()

        return data 
