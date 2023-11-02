import mysql.connector
from db.base_controller import BaseController

class PlayersController(BaseController):
    """
    Class that manage the tournament.players

    ...

    Methods
    -------

    select_players_by_club(club_name: str, season: str)
        Select all players with contract with a specific club
    select_players_with_contract(season: str)
        Select all players with contract with a club
    """
        
    @classmethod
    def select_players_by_club(cls, club_name: str, season: str) -> list[set]:
        """Select players with contract of a club

        Parameters
        ----------
        
        club_name : str
            Club's name that will be used as parameter to the players
        season : str
            Season that will be used as parameter to player_contracts extension

        Returns
        -------
            A list of Players data 
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_players_by_clubs'), [club_name, season])
        players = cursor.fetchall()

        return players

    @classmethod
    def select_players_with_contract(cls, season: str) -> list[set]:
        """Select all players that have a contract with a club

        Parameters
        ----------

        season : str
            Season that will be used as parameter to player_contracts extension

        Returns
        -------
            A list of Players data 
        """        

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_players_by_contracts'), [season])
        players = cursor.fetchall()

        return players


if __name__ == "__main__":
    print(PlayersController().select_players_by_club('2022'))
