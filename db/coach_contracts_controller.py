import mysql.connector
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
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for coach_contract in coach_contracts_data:
            cursor.execute(cls.get_insert_query('insert_coach_contracts'), coach_contract)
        
        conn.commit()
        conn.close()

        return None 
    