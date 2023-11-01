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
        self.id = id
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()

        self.squad = []
        self.start_eleven = []
        self.bench = []

    def __repr__(self):
        return f"Club({self.name})"
    
    def add_to_squad(self, *values: list):
        self.squad += values

    def add_to_start_eleven(self, *values: list):
        self.start_eleven += values 
    
    def add_to_bench(self, *values: list):
        self.bench += values