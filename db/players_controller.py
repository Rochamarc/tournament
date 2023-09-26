import mysql.connector
from db.base_controller import BaseController

class PlayersController(BaseController):
    @classmethod
    def select_players_by_club(cls, club_name: str, season: str) -> list[set]:
        ''' Select players by club_name and season clause 
            club_name -> club on player_contracts
            season -> overall on overall
        '''

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_players_by_clubs'), [club_name, season])
        players = cursor.fetchall()

        return players

if __name__ == "__main__":
    print(PlayersController().select_players_by_club('Coritiba'))
