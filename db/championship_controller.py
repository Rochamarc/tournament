import mysql.connector
from db.base_controller import BaseController

class ChampionshipsController(BaseController):
    @classmethod
    def select_championship_table_by_club(cls, season: int, club_id: int) -> list[set]:
        ''' Select championship club table by club '''
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_championship_by_club'), [club_id, season])
        values = cursor.fetchall()

        conn.close()
        return values

    @classmethod
    def update_championship_table(cls, season: str, club_id: int, update_data: list) -> None:
        ''' Update championships table in database
            season: the season of the table to be updated
            club_id: club that will have the table updated
            update_data: [ matches, won, draw, lost, goals_for, goals_away, goall_diff ] 
                list of values to be updated in the list
        '''
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        update_data += [club_id, season]

        cursor.execute(cls.get_update_query('update_championship'), update_data)
        
        conn.commit()
        conn.close()

        return None

