import sqlite3 

from db.open_query import QueryHelper

database = 'database.db'

qh = QueryHelper()


class ClubData():
    @staticmethod
    def insert_clubs_db(clubs, verbose=False):
        '''
        Insert clubs into the databse
        '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        print('Inserting clubs into the database')

        for club in clubs:
            print('.', sep=' ', end=' ', flush=True)

            if verbose : print(f"Insert club {club} into the database")

            club_data = club.data() # get the club info

            cursor.execute("INSERT INTO clubs (name, country, state, coeff, club_class, formation, total_budget, salary_budget) values (?,?,?,?,?,?,?,?)", club_data)
            
        conn.commit()
        conn.close()

        if verbose : print("Players inserted into the database sucessfully!")
        return True

    @staticmethod
    def get_clubs(clubs, verbose=False):
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
    def get_clubs_by_country(country):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
    
        val = cursor.execute("SELECT * FROM clubs WHERE country=?", (country, )).fetchall()
        data = val.copy()

        conn.close()
        return data 