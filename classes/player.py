from classes.person import Person 

class Player(Person):

    def __init__(self, id: int, name: str, nationality: str, age: int, position: str, height: float, weight: float, foot: str, retirement: str= 'False'):
        super().__init__(name, nationality, age)
        self.id = id
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

