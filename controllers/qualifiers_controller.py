from controllers.base_controller import BaseController

class QualifiersController(BaseController):
    """
    """

    @classmethod
    def insert_qualifiers(cls, season: str, clubs: list, phase: str, competition_id: int) -> None:
        """Insert a list of clubs qualifiers to a phase of a competition

        Parameters
        ----------
        season : str
            A string containing a season
        clubs : list
            A list of ids of clubs
        phase : str
            A string with phase name
        competition_id : int
            A int value for a competition id
        
        Returns
        -------
            None
        """
        
        for club in clubs:
            cls.insert_register(cls.get_query('insert','qualifiers','qualifiers'), [season, phase, club, competition_id])

        return None