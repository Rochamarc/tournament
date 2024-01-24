from controllers.base_controller import BaseController

class MarketController(BaseController):
    """
    Class that manages a series of joins to get player info to football market 
    
    Methods
    -------
    search_by_overall(overall: int, season: int)
        Select a list of players by overall
    search_by_age(age: int, season: int)
        Select a list of players by age
    search_by_position(position: str, season: int)
        Select a list of players by position
    search_by_all(position: str, overall: int, season: int)
        Select a list of players by position & overall
    """
    
    @classmethod
    def search_by_overall(cls, overall: int, season: int) -> list[set]:
        """Make a search on the database for players by overall

        Parameters
        ----------
        overall : int
            An int value that will be equal or higher on the search
        season : int
            An int value for the season that you wanna do the search
        
        Return
        ------
            A list of sets with player's id, nationality, position, age, hight, foot, overall, market_value, salary and current_club
        """

        return cls.select_register(cls.get_query('select', 'market', 'player_info_by_overall'), [season, overall])
    
    @classmethod
    def search_by_age(cls, age: int, season: int) -> list[set]:
        """Make a search on the database for players by overall

        Parameters
        ----------
        age : int
            An int value that will be equal on the search
        season : int
            An int value for the season that you wanna do the search
        
        Return
        ------
            A list of sets with player's id, nationality, position, age, hight, foot, overall, market_value, salary and current_club
        """
        
        return cls.select_register(cls.get_query('select', 'market', 'player_info_by_age'), [season, age])

    @classmethod
    def search_by_position(cls, position: str, season: int) -> list[set]:
        """Make a search on the database for players by overall

        Parameters
        ----------
        position : str
            A string value that will be equal on the search
        season : int
            An int value for the season that you wanna do the search
        
        Return
        ------
            A list of sets with player's id, nationality, position, age, hight, foot, overall, market_value, salary and current_club
        """

        return cls.select_register(cls.get_query('select', 'market', 'player_info_by_position'), [season, position])
    
    @classmethod
    def search_by_all(cls, position: str, overall: int, season: int) -> list[set]:
        """Make a deep search on the database for players by position and overall

        Parameters
        ----------
        position : str
            A string value that will be equal on the search
        overall : int
            An int value that will be equal or higher on the search
        season : int
            An int value for the season that you wanna do the search
        
        Return
        ------
            A list of sets with player's id, nationality, position, age, hight, foot, overall, market_value, salary and current_club
        """

        return cls.select_register(cls.get_query('select', 'market', 'player_info_by_all'), [season, overall, position])
        