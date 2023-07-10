import sqlite3 

from db.open_query import QueryHelper

database = 'database.db'

qh = QueryHelper()

class DomesticLeague():
    @staticmethod
    def create_domestic_table(division, season, verbose=False):
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

            cursor.execute(f"INSERT INTO campeonato_brasileiro_{division}_{season} (club, matches, won, draw, lost, goals_for, goals_away, goal_diff, points) VALUES (?,?,?,?,?,?,?,?,?)", ls)
        
        conn.commit()
        conn.close()

            
        if verbose : print("Database populada com sucesso!")

        return True 

    @staticmethod
    def update_domestic_table(club_stats, division, season):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        division.replace(' ', '_')

        cursor.execute(f"""
            UPDATE campeonato_brasileiro_{division}_{season} 
            SET matches=matches+1, 
                won=won + ?,
                draw=draw + ?,
                lost=lost + ?,
                goals_for=goals_for + ?,
                goals_away=goals_away + ?,
                goal_diff=goal_diff + ?,
                points=points + ?
            WHERE club = ?
        """, club_stats)
        
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
