from controllers.base_controller import BaseController

class CompetitionsController(BaseController):
    """Class that handle tournament.competitions & divisions

    ...

    Methods
    -------
    select_competition_id(competition_name: str)
        Select competition id based on name
    """
    
    @classmethod
    def insert_divisions(cls, divisions: list) -> None:
        """Insert registers into tournament.divisions

        Parameters
        ----------
        divisions : list
            A list with division name and competition id
        
        Returns
        -------
        None
        """

        cls.insert_registers(
            cls.get_query('insert', 'competitions', 'divisions'),
            divisions,
        )
    
        return None
    
    @classmethod
    def insert_competitions(cls, competitions: list[str]) -> None:
        """Insert registers into tournament.competitions

        Parameters
        ----------
        competitions : list
            A list with competitions names
        
        Return
        ------
            None
        """
        
        cls.insert_registers(
            cls.get_query('insert', 'competitions', 'competitions'), 
            competitions,
            complex=False
            )
    
        return None 

    @classmethod
    def select_competition_id(cls, competition_name: str) -> list[set]:
        """Select the id from tournament.competitions

        Parameters
        ----------
        competition_name : str
            A string containing the name of competition

        Returns
        -------
            A list with a set containing the id from competition
        """

        return cls.select_register(cls.get_query('select','competitions','competition_id'), [competition_name])
        