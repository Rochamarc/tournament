import sqlite3 

database = 'database.db'

class CoachData():
    @staticmethod
    def coach_sacking(coach):
        '''
        Remove the club name from coach's current_club table
        '''
        pass 


    @staticmethod
    def insert_coaches_db(coaches):   
        '''
        Insert coaches into the database
        list(coachs) [ name, nationality, age, formation, play_mode, current_club ]
        '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for coach in coaches:
            cursor.execute("INSERT INTO coach (name, nationality, age, formation, play_mode, current_club) VALUES (?,?,?,?,?,?)", coach)
        
        conn.commit()
        conn.close()

        print('Coaches inserted sucessfully')

    @staticmethod
    def get_all_coaches():

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        data = cursor.execute("SELECT * FROM coach").fetchall()

        return data
