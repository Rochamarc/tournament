import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class CompetitionData():
    @staticmethod 
    def insert_champion_db(competition, club, season):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(qh.open_insertion_query('competition'), [competition, club, season])        

        conn.commit()
        conn.close()

        return True 