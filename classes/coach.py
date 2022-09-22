from classes.person import Person

from random import choice

class Coach(Person):
    def __init__(self, name, nationality, age):
        super().__init__(name, nationality, age)
        self.formation = None 
        self.play_mode = None
        
        self.salary = None
        
    def technical_features(self):
        ''' Define the coach technical features as his attacking mode and formation '''
        att = choice(['offensive', 'defensive'])
        
        if att == 'offensive':
            self.formation = choice(['4-3-3', '4-4-2'])
        else:
            self.formation = choice(['3-5-2', '3-4-3'])
        
        self.play_mode = att

    def __repr__(self):
        return f"Coach({self.name})"

    def __str__(self):
        return f"Coach({self.name})"

    @property
    def data(self):
        return {
            "name": self.name,
            "nationality": self.nationality,
            "age": self.age,
            "formation": self.formation,
            "play_mode": self.play_mode,
            "current_club": f"http://still-wave-44749.herokuapp.com/clubs/{club_api.get_club_by_name(self.current_club)['id']}/",
            "salary": self.salary
        }