import mysql.connector

from db.open_query import QueryHelper
from db.database import export_database_config

qh = QueryHelper()

class StadiumData():
    @staticmethod
    def insert_stadiums_db(stadiums: list) -> None:
        ''' Insert stadiums to the database ''' 
        
        conn = mysql.connector.connect(**export_database_config())
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

        conn = mysql.connector.connect(**export_database_config())
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM stadium")
        re = cursor.fetchall()

        #data = val.copy()
        conn.close()

        return re
