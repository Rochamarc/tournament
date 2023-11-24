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
    select_all_players_id_position()
        Select all the player's id and position of tournament.players
    select_players_by_club(club_name: str, season: str)
        Select all players with contract with a specific club
    select_players_with_contract(season: str)
        Select all players with contract with a club
    delete_players()
        Delete all players from database
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
        
        return cls.insert_registers(cls.get_insert_query('insert_players'), players_data)

    @classmethod
    def select_last_players(cls) -> list:
        """Select the last players from tournament.players

        Returns
        -------
            A list with 30 length containing player information
        """

        return cls.select_register(cls.get_select_query('select_last_players'))
        
    @classmethod
    def select_all_players_id(cls) -> list:
        """Select the player's id from tournament.players

        Returns
        -------
            A list of sets with (id,) column from the tournament.players
        """
        
        return cls.select_register(cls.get_select_query('select_id_from_players'))

    @classmethod
    def select_all_players_id_position(cls) -> list[set]:
        """Select the player's id and position from tournament.players 

        Returns
        -------
            A list of sets with (id, position,) from tournament.players
        """

        return cls.select_register(cls.get_select_query('select_id_position_from_players'))


    @classmethod
    def select_players_by_club(cls, club_name: str, season: str) -> list[set]:
        """Select players with contract of a club, this aggregates players table
        with player_contracts, clubs & skills

        Parameters
        ----------
        
        club_name : str
            Club's name that will be used as condition to clubs.name
        season : str
            Season that will be used as parameter to player_contracts & skills

        Returns
        -------
            A list of Players data 
        """

        return cls.select_register(cls.get_select_query('select_players_by_clubs'), [club_name, season])


    @classmethod
    def select_players_with_contract(cls, season: str) -> list[set]:
        """Select all players that have a contract with a club, this aggregates players table
        with player_contracts, clubs & skills

        Parameters
        ----------

        season : str
            Season that will be used as parameter to player_contracts & skills

        Returns
        -------
            A list of Players data 
        """        

        return cls.select_register(cls.get_select_query('select_players_by_contracts'), [season])

    @classmethod
    def delete_players(cls) -> None:
        """Delete all players and his constraints

        Returns
        -------
            None
        """

        return cls.delete_register(cls.get_delete_query('delete_players'))



if __name__ == "__main__":
    print(PlayersController().select_players_by_club('2022'))
