import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class DomesticLeague():
    @staticmethod
    def create_domestic_table(division, season, verbose=False):
        ''' Create domestic table '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        division.replace(' ', '_')

        if verbose : print(f"Criando tabela da copa doméstica {division} {season}")

        cursor.execute(qh.open_create_query('brasileirao').format(division, season))


        conn.close() # close database

        if verbose : print("Tabela criada com sucesso")
    
    @staticmethod
    def domestic_table_basic(club_names, division, season, verbose=False):
        '''
        Insert club domestic cup data into the database
        '''

        division.replace(' ', '_')

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        
        print("Inserting clubs into domestic cup table")

        for club in club_names:
            print('.', sep=' ', end=' ', flush=True)

   
            ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]

            if verbose : print(f"Inserting {club} into the database.")

            cursor.execute(qh.open_insert_query('brasileirao').format(division, season), ls)
        
        conn.commit()
        conn.close()

            
        if verbose : print("Database populada com sucesso!")

        return True 

    @staticmethod
    def update_domestic_table(club_stats, division, season):
        ''' Update values from domestic table '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        division.replace(' ', '_')

        cursor.execute(qh.open_update_query('brasileirao').format(division, season), club_stats)
        
        conn.commit()
        conn.close()

    @staticmethod
    def get_domestic_cup_table(division, season):
        ''' Get the domestic cup table data '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute(f"""
            SELECT * FROM campeonato_brasileiro_{division}_{season} 
            ORDER BY 
                points DESC, 
                goals_for DESC, 
                goal_diff DESC
            """).fetchall()
        
        data = val.copy() # create a copy of the fetch data
        conn.close()
        
        return data
