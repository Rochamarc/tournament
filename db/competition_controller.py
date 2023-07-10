import sqlite3 

database = 'db/database.db'

class CompetitionData():
    @staticmethod 
    def insert_champion_db(competition, club, season):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO champion (competition, club, season) VALUES (?,?,?)", [competition, club, season])        

        conn.commit()
        conn.close()

        return True 