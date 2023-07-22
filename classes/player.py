from classes.person import Person 

from random import choice, randint, triangular

class Player(Person):

    def __init__(self, name: str, nationality: str, age: int, position: str, min_coeff: int, max_coeff: int, retirement: str= 'False', current_club=None):
        super().__init__(name, nationality, age)
        self.__overall = randint(min_coeff, max_coeff)
        self.current_club = current_club
        self.current_club_id = None
        self.position = position
    
        self.retirement = retirement

        #stats de competição
        self.matches_played = 0
        self.goals = 0
        self.assists = 0
        self.points = 0  # every match another point is add here, thent is calculated by the average

        # physical
        self.height = self.set_height() 
        self.weight = float("{:.2f}".format(triangular(65.0, 90.0)))
        self.foot = choice(['Right', 'Left'])

        # finances
        self.market_value = randint(10_000, 80_000_000)
        self.salary = randint(1_000, 500_000)

        self.average = 0

    
    @property
    def overall(self) -> int:
        return self.__overall
 
    def insert_overall(self, external_overall: int) -> None:
        self.__overall = external_overall

    @property
    def avg(self) -> float:
        try:
            return (round((self.points / self.matches_played), 1))
        except:
            return 0.0
    
    def set_height(self) -> float: 
        if self.position == 'GK':
            return float("{:.2f}".format(triangular(1.79, 1.98)))
        elif self.position == 'CB':
            return float("{:.2f}".format(triangular(1.75, 1.88)))
        elif self.position in ['LB', 'RB']:
            return float("{:.2f}".format(triangular(1.65, 1.80)))
        elif self.position == 'CF':
            return float("{:.2f}".format(triangular(1.75, 1.90)))
        else:
            return float("{:.2f}".format(triangular(1.65, 1.89)))

    def get_competition_stats(self) -> list:
        ''' return matches_played, goals, assists, points '''
        return [ self.matches_played, self.goals, self.assists, self.points, self.id ] 

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player({self.name})'

    def data(self) -> list:
        ''' Return all player data '''
        return [
            self.name, self.nationality, self.age, self.overall, self.current_club,
            self.position, self.matches_played, self.goals, self.assists, self.avg, 
            self.market_value, self.salary, self.height, self.weight, self.foot
        ]

    def data_season(self) -> list:
        ''' Return a list oriented to players season '''
        return [
            self.name, self.nationality, self.age, self.overall, self.current_club,
            self.position, self.matches_played, self.goals, self.assists, self.points,
            self.avg, self.market_value, self.salary
        ]
        
    def increase_overall(self):
        ''' Increase overall by one '''
        self.__overall += 1

    def decrease_overall(self):
        ''' Decrease overall by one '''
        self.__overall -= 1
