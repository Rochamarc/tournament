from db.base_controller import BaseController

class PlayerContractsController(BaseController):
    """
    Class that manage the tournament.player_contracts

    ...

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