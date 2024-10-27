# start_eleven -> will have to be another type of data storage because it only accept 11
#
#

class Club:
    """
    A class that represents a Football/Soccer Club

    ...

    Attributes
    ----------
    id :  int
        Unique value the representes each club
    name : str
        The name of the club
    country : str
        The nationality from the club
    short_country : str
        The three initials letters from the club's country
    squad : list
        A list of every athlete that plays for the club
    start_eleven : list
        A list of the 11 players that start the matches
    bench : list
        A list of the remaining players
    overall : int
        A value of the clubs players overall average

    Methods
    -------
    add_to_squad(values: list)
        Add players to the squad
    add_to_start_eleven(values: list)
        Add players to start_eleven
    add_to_bench(values: list)
        Add players to bench
    """
    
    def __init__(self, id: int, name: str, country: str):
        self.__id = id
        self.__name = name
        self.__country = country
        self.__short_country = country[:3].upper()

        self.__squad = []
        self.__start_eleven = []
        self.__bench = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def country(self) -> str:
        return self.__country

    @property
    def short_country(self) -> str:
        return self.__short_country

    @property
    def squad(self) -> list:
        """Return a copy of the original list
        """
        return self.__squad.copy()
    
    @property
    def start_eleven(self) -> list:
        """Return a copy of the original list
        """
        return self.__start_eleven.copy()

    @property
    def bench(self) -> list:
        """Return a copy of the original list
        """
        return self.__bench.copy()

    def __repr__(self):
        return f"Club({self.__name})"

    @start_eleven.setter
    def start_eleven(self, other_value: list) -> None:
        self.__start_eleven = other_value

    @bench.setter 
    def bench(self, other_value: list) -> None:
        self.__bench = other_value

    def add_to_squad(self, *values: list):
        """Add players to squad

        Attributes
        ----------
        values : list
            A list of players's objects

        Returns
        -------
            None
        """
        
        self.__squad += values

    def add_to_start_eleven(self, *values: list):
        """Add players to start eleven

        Attributes
        ----------
        values : list
            A list of players's objects

        Returns
        -------
            None
        """
        
        self.__start_eleven += values 
    
    def add_to_bench(self, *values: list):
        """Add players to bench

        Attributes
        ----------
        values : list
            A list of players's objects

        Returns
        -------
            None
        """

        self.__bench += values
    
    @property
    def overall(self):
        """Return the aritmetic average of the squad's overall

        Returns
        -------
            A int value of the aritmetic average squad overall 
        """
        if len(self.squad) == 0:
            return 0
        return round(sum([ player.overall for player in self.squad ]) / len(self.squad))