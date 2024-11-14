from classes.habilities import Hability

class Player(Hability):
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
    positioning : int
        A integer that value for player positioning GK only
    reflexes : int
        A integer that value for player reflexes GK only
    diving : int
        A integer that value for player diving GK only
    standing_tackle : int
        A integer that value for player standing tackle Non GK players
    physical : int
        A integer that value for player physical Non GK players
    passing : int
        A integer that value for player passing Non GK players
    dribbling : int
        A integer that value for player dribbling Non GK players
    long_shot : int
        A integer that value for player long shot Non GK players
    finishing : int
        A integer that value for player finishing Non GK players
    club_id : int
        The id from the club that the athlete plays for 
    
    Properties
    ----------
    name
    nationality
    id
    club_id
    foot
    height
    weight

    Methods
    -------
    age(year: int)
        Calculates players age
    """

    def __init__(self, id: int, name: str, nationality: str, birth: int, position: str, 
                 height: float, weight: float, foot: str, positioning: int, reflexes: int, 
                 diving: int, standing_tackle: int, physical: int, passing: int,
                 dribbling: int, long_shot: int, finishing: int, club_id: int):
        
        super().__init__(position, positioning, reflexes, diving, standing_tackle, physical, passing, dribbling, long_shot, finishing)

        self.__name = name 
        self.__nationality = nationality
        self.__birth = birth 

        self.__id = id
        self.__height = height
        self.__weight = weight
        self.__foot = foot
        self.__club_id = club_id
        self.__hash = None

    @hash.setter
    def hash(self, hash_value: set[float]) -> None:
        self.__hash = hash_value

    @property
    def hash(self) -> set[float]:
        return self.__hash
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def nationality(self) -> str:
        return self.__nationality
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def club_id(self) -> int:
        return self.__club_id
    
    @property
    def foot(self) -> str:
        return self.__foot

    @property
    def height(self) -> float:
        return self.__height
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    def age(self, year: int) -> int:
        """Show player's age

        Parameters
        ----------
        year : int
            A four digit value for a year
        
        Returns
        -------
        int : Value for the player age
        """

        return year - self.__birth
    
    def transfer(self, new_club_id: int) -> None:
        """Change the player's club
        
        Returns
        -------
            None
        """
        
        self.__club_id = new_club_id

    def __repr__(self):
        return f'Player({self.__name})'

    def __str__(self):
        return f'Player({self.__name})'

if __name__ == "__main__":
    ...