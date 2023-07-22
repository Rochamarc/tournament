import sqlite3 

from db.open_query import QueryHelper

database = 'db/database.db'

qh = QueryHelper()

class InternationalCup():

    @staticmethod
    def create_international_cup(season: str, group: str) -> None:
        ''' Create libertadores table '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(qh.open_create_query('libertadores').format(group, season))
        conn.close() # close database
        
        return None

    @staticmethod
    def update_international_table(club_stats: list, group: str, season: str) -> None:
        ''' Update values from libertadores table '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(qh.open_update_query('libertadores').format(group, season), club_stats)

        conn.commit()
        conn.close()
        return None 
    
    @staticmethod
    def international_group_table_basic(club_names: list,season: str, group: str) -> None:
        ''' Insert data into libertadores table '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        for club in club_names:
            ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]

            cursor.execute(qh.open_insert_query('libertadores').format(group, season), ls)
        
        conn.commit()
        conn.close()

        return None

    @staticmethod
    def get_group_stage_data(season: str) -> dict:
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
