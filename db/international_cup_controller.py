import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class InternationalCup():

    @staticmethod
    def create_international_cup(season, group, verbose=False):
        ''' Create libertadores table '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        if verbose : print(f"Criando tabela da copa doméstica {season} {group}")

        cursor.execute(qh.open_create_query('libertadores').format(group, season))

        conn.close() # close database

        if verbose : print("Tabela criada com sucesso")
        return True

    @staticmethod
    def update_international_table(club_stats, group, season):
        ''' Update values from libertadores table '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(qh.open_update_query('libertadores').format(group, season), club_stats)

        conn.commit()
        conn.close()
        return True 
    
    @staticmethod
    def international_group_table_basic(club_names,season, group, verbose=False):
        ''' Insert data into libertadores table '''

        print("Inserting clubs into domestic cup table")

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for club in club_names:
            print('.', sep=' ', end=' ', flush=True)


            ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]

            if verbose : print(f"Inserting {club} into the database.")

            cursor.execute(qh.open_insert_query('libertadores').format(group, season), ls)
        
        conn.commit()
        conn.close()
    
        if verbose : print("Database populada com sucesso!")

        return True

    @staticmethod
    def get_group_stage_data(season) -> dict:
        ''' 
        Get international cup group stage 
        return dict { 'A' : [data], ... }
        '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        full_data = {}

        for group in groups:
            g = f'group_{group}'

            val = cursor.execute(f"""
                SELECT * FROM libertadores_{g}_{season}
                ORDER BY 
                    points DESC, 
                    goals_for DESC, 
                    goal_diff DESC
                """).fetchall()

            data = val.copy() # create a copy of the fetch data
            full_data[group] = data
        conn.close()
        
        return full_data
