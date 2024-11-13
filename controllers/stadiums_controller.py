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
    def insert_stadiums(cls, stadiums_data: list) -> None:
        """Insert a list of stadiums data: name, capacity, country, city

        Parameters
        ----------
        stadiums_data : list
            A list of real stadiums data
        
        Returns
        -------
        None
        """

        cls.insert_registers(
            cls.get_query('insert', 'stadiums', 'stadiums'),
            stadiums_data
        )

        return None
     
    @classmethod
    def insert_generic_stadiums(cls, stadiums_data: list) -> None:
        """Insert generic stadiums without city name

        Parameters
        ----------
        stadiums_data : list
            A list with generic stadiums data

        Returns
        -------
        None
        """

        cls.insert_registers(
            cls.get_query('insert', 'stadiums', 'generic_stadiums'),
            stadiums_data
        )

        return None

    @classmethod
    def insert_stadiums_ownership(cls, data: list) -> None:
        """Insert stadium ownerships

        Parameters
        ----------
        data : list
            Stadium's and club's id 
        """

        cls.insert_registers(
            cls.get_query('insert', 'stadiums', 'stadium_ownership'),
            data
        )
        return None
    
    @classmethod
    def select_all_stadiums(cls) -> list[set]:
        """Select all stadiums from database
        
        Returns
        -------
            A list of lists with stadium data
        """

        return cls.select_register(cls.get_query('select','stadiums','stadiums'))