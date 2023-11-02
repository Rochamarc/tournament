import mysql.connector
from db.base_controller import BaseController

class PlayersController(BaseController):
    """
    Class that manage the tournament.players

    ...

    Methods
    -------
    insert_players(players_data: list)
        Insert a list of tournament.players in database
    select_last_players()
        Select the 30 last tournament.players inserted
    select_all_players_id()
        Select all the player's id of tournament.players
    select_players_by_club(club_name: str, season: str)
        Select all players with contract with a specific club
    select_players_with_contract(season: str)
        Select all players with contract with a club
    """
        
    @classmethod
    def insert_players(cls, players_data: list) -> None:
        """Insert a list of players_data into tournament.players

        Parameters
        ----------
        players_data : list
            A list of lists containing: name: str, nationality: str, position: str, birth: int, height: float, weight: float, foot: str
        
        Returns
        -------
            None
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for player_data in players_data:
            cursor.execute(cls.get_insert_query('insert_players'), player_data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def select_last_players(cls) -> list:
        """Select the last players from tournament.players

        Returns
        -------
            A list with 30 length containing player information
        """
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_last_players'))
        players = cursor.fetchall()

        return players
        
    @classmethod
    def select_all_players_id(cls) -> list:
        """Select the player's id from tournament.players

        Returns
        -------
            A list with the id column from the tournament.players
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_id_from_players'))
        players = cursor.fetchall()

        return players

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
