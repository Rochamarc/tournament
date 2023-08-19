from classes.person import Person 

class Player(Person):

    def __init__(self, name: str, nationality: str, age: int, position: str, overall: int, height: float, weight: float, foot: str, retirement: str= 'False', current_club=None):
        super().__init__(name, nationality, age)
        self.overall = overall
        self.current_club = current_club
        self.current_club_id = None
        self.position = position
    
        self.retirement = retirement

        # physical
        self.height = height
        self.weight = weight
        self.foot = foot

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player({self.name})'

