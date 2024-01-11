from db.base_controller import BaseController

class PlayerContractsController(BaseController):
    """
    Class that manage the tournament.player_contracts

    Methods
    -------
    insert_player_contracts(player_contracts_data: list)
        Insert a list of tournament.player_contracts in database
    """

    @classmethod
    def insert_player_contracts(cls, player_contracts_data: list) -> None:
        """Insert a list of player_contracts_data into tournament.player_contracts

        Parameters
        ----------
        player_contracts_data : list
            A list of lists containing: 
            start: str, end: str, salary: int, club_id: int, player_id: int
        
        Returns
        -------
            None
        """
        
        return cls.insert_registers(cls.get_query('insert', 'insert_player_contracts'), player_contracts_data)

    @classmethod
    def select_players_with_no_contract(cls) -> list[set]:
        """Select a list of Free Agent players data from tournament.player_contracts

        Returns
        -------
            A list of sets with [player_contracts.id, players.id]
        """

        return cls.select_register(cls.get_query('select','select_players_with_no_contract'))

    @classmethod
    def select_players_with_end_contract(cls, season: str) -> list[set]:
        """Select a list of Free Agent players data from tournament.player_contracts

        Parameters
        ----------
        season : str
            An string value with end of season 
        
        Returns
        -------
            A list of sets with [player_contracts.id, players.id]
        """

        return cls.select_register(cls.get_query('select', 'select_players_with_end_contract'), season)