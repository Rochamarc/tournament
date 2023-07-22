import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()


class ClubData():
    @staticmethod
    def insert_clubs_db(clubs, verbose=False):
        '''
        Insert clubs into the databse
        '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        if verbose: print('Inserting clubs into the database')
        
        if verbose : print(f"Insert club {club} into the database")

         
        for club in clubs:
            club_data = club.data() 
            cursor.execute(qh.open_insert_query('clubs'), club_data)
        

        conn.commit()
        conn.close()

        if verbose : print("Clubs inserted into the database sucessfully!")
        return True

    @staticmethod
    def get_clubs(clubs) -> list:
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