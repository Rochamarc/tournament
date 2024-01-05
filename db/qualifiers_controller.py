from db.base_controller import BaseController

class QualifiersController(BaseController):
    """
    """

    @classmethod
    def insert_qualifiers(cls, clubs: list, phase: str, competition_id: int) -> None:
        """Insert a list of clubs qualifiers to a phase of a competition

        Parameters
        ----------
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
            cls.insert_register(cls.get_query('insert','insert_qualifiers'), [phase, club, competition_id])

        return None