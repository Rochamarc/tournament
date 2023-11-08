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
        gk_average
            Calculates goal keeper skills average
        defense_average
            Calculates defensive players skills average
        attacking_average
            Calculates defensive players skills average
        overall
            Calculates full players skills average
    """

    def __init__(self, id: int, name: str, nationality: str, birth: int, position: str, 
                 height: float, weight: float, foot: str, positioning: int, reflexes: int, 
                 diving: int, standing_tackle: int, physical: int, passing: int,
                 dribbling: int, long_shot: int, finishing: int, club_id: int):
        
        super().__init__(name, nationality, birth)
        self.id = id
        self.position = position

        # physical
        self.height = height
        self.weight = weight
        self.foot = foot

        self.club_id = club_id
        
        # skills
        self.positioning = positioning 
        self.reflexes = reflexes
        self.diving = diving
        self.standing_tackle = standing_tackle
        self.physical = physical
        self.passing = passing 
        self.dribbling = dribbling
        self.long_shot = long_shot
        self.finishing = finishing

    @property
    def gk_average(self) -> int:
        '''Calculates the goal keeper average
        
        Returns
        -------
            Average of position, reflexes & diving
        '''

        return (self.position + self.reflexes + self.diving) // 3
    
    @property
    def defense_overall(self) -> int:
        '''Calculates the defensive players average
        
        Returns
        -------
            Average of stading_tackle, physical & passing
        '''

        return (self.standing_tackle + self.physical + self.passing) // 3

    @property
    def attacking_overall(self) -> int:
        '''Calculates the attacking players average

        Returns
        -------
            Average of driblling, long_shot & finishing
        '''
        
        return (self.dribbling + self.long_shot + self.finishing) // 3

    @property
    def overall(self) -> int:
        '''Calculates the full skill players average
        
        Returns
        -------
            gk_average if is a goalkeeper. the full average if it's not. 
        
        TODO add weighted average to the position that are being calculated ex: self.defense_overall * 2 if the player are defensive
        '''
        
        if self.position == 'GK':
            return self.gk_average
        return (self.standing_tackle + self.physical + self.passing + self.dribbling + self.long_shot + self.finishing) // 6
    
    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player({self.name})'
