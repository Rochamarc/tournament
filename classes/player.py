from classes.person import Person 

class Player(Person):
    def __init__(self, id: int, name: str, nationality: str, birth: int, position: str, height: float, weight: float, foot: str, overall: int):
        super().__init__(name, nationality, birth)
        self.id = id
        self.position = position

        # physical
        self.height = height
        self.weight = weight
        self.foot = foot
        self.overall = overall        

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player({self.name})'
