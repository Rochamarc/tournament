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
        