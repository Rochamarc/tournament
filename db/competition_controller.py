import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class CompetitionData():
    @staticmethod 
    def insert_champion_db(competition: str, club: str, season: str) -> None:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(qh.open_insert_query('competition'), [competition, club, season])        

        conn.commit()
        conn.close()

        return None 