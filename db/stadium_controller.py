import sqlite3 

database = 'database.db'

class StadiumData():
    @staticmethod
    def insert_stadiums_db(stadiums, verbose=False):
        ''' Insert stadiums to the database '''
        
        print("Inserting stadiums into the database ")
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        for stadium in stadiums:
            print('.', sep=' ', end=' ', flush=True)

            if verbose : print(f"Insert stadium {stadium} into the database")



            std_data = stadium.data

            cursor.execute("INSERT INTO stadium (name, location, capacity, club_owner) VALUES (?,?,?,?)", std_data)

        conn.commit()
        conn.close()

        if verbose : print("Stadiums inserted into the database sucessfully!")
        return True

    @staticmethod
    def get_stadiums():
        ''' Get stadiums data '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute("SELECT name, location, capacity, club_owner FROM stadium").fetchall()

        data = val.copy()
        conn.close()

        return data 
