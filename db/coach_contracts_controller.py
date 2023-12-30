from db.base_controller import BaseController

class CoachContractsController(BaseController):
    """
    Class that manage the tournament.coach_contracts

    ...

    Methods
    -------
    insert_coach_contracts(coach_contracts_data: list)
        Insert a list of tournament.coach_contracts in database
    """

    @classmethod
    def insert_coach_contracts(cls, coach_contracts_data: list) -> None:
        """Insert a list of player_contracts_data into tournament.coach_contracts

        Parameters
        ----------
        coach_contracts_data : list
            A list of lists containing: 
            start: str, end: str, salary: int, club_id: int, coach_id: int
        
        Returns
        -------
            None
        """

        return cls.insert_registers(cls.get_query('insert', 'insert_coach_contracts'), coach_contracts_data)
         
    