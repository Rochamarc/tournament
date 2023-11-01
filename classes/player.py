from classes.person import Person 

class Player(Person):
    """
    A class that represents a Football/Soccer player

    ...

    Attributes
    ----------
        id :  int
            Unique value the representes each coach
        name : str
            The name of the coach
        nationality : str
            The nationality from the coach
        birth : int
            The birth year of the coach
        position : str
            Two capital letters that represents the players position
        height : float
            Players height
        weight : float
            Players weight
        foot : str
            A capital letter that represents the player favorite foot
        overall : int
            A value from 56 to 100 that represents how good the player is
        club_id : int
            The id from the club that the athlete plays for 
    """

    def __init__(self, id: int, name: str, nationality: str, birth: int, position: str, height: float, weight: float, foot: str, overall: int, club_id: int):
        super().__init__(name, nationality, birth)
        self.id = id
        self.position = position

        # physical
        self.height = height
        self.weight = weight
        self.foot = foot
        self.overall = overall        

        self.club_id = club_id
        
    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player({self.name})'
