from controllers.base_controller import BaseController

class StadiumsController(BaseController):
    """
    Class that manage the tournament.stadiums

    ...

    Methods
    -------

    select_all_stadiums()
        Select all stadiums from database
    """
        
    @classmethod
    def select_all_stadiums(cls) -> list[set]:
        """Select all stadiums from database
        
        Returns
        -------
            A list of lists with stadium data
        """

        return cls.select_register(cls.get_query('select','stadiums','stadiums'))