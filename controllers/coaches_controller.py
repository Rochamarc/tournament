from controllers.base_controller import BaseController

class CoachesController(BaseController):
    """
    Class that manage the tournament.coaches

    ...

    Methods
    -------
    insert_coaches(coaches_data: list)
        Insert a list of tournament.coaches in database
    select_id()
        Select all coach's id
    """

    @classmethod
    def insert_coaches(cls, coaches_data: list) -> None:
        """Insert a list of coaches_data into tournament.coaches

        Parameters
        ----------
        coaches_data : list
            A list of lists containing: 
            name: str, nationality: str, birth: int
        
        Returns
        -------
            None
        """

        return cls.insert_registers(cls.get_query('insert', 'insert_coaches'), coaches_data)


    @classmethod
    def select_id(cls) -> list[set]:
        """Select id from coaches

        Returns
        -------
            A list of lists with: id
        """

        return cls.select_register(cls.get_query('select','select_id_from_coaches')) 

    @classmethod
    def delete_coaches(cls) -> None:
        """Delete all coaches and his constraints

        Returns
        -------
            None
        """

        return cls.delete_register(cls.get_query('delete', 'delete_coaches'))

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
         
    