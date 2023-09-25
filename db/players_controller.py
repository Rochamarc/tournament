import mysql.connector
from base_controller import BaseController

class PlayersController(BaseController):
    @classmethod
    def select_players_by_club(cls, club_name: str) -> list[set]:
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_players_by_clubs'), [club_name])
        players = cursor.fetchall()

        return players

if __name__ == "__main__":
    print(PlayersController().select_players_by_club('Coritiba'))
