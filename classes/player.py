from classes.person import Person 

from random import choice, randint, triangular

class Player(Person):

    def __init__(self, name, nationality, age, position, min_coeff, max_coeff, current_club=None):
        super().__init__(name, nationality, age)
        self.__overall = randint(min_coeff, max_coeff)
        self.current_club = current_club
        self.current_club_id = None
        self.position = position

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
    def overall(self):
        return self.__overall
 
    def insert_overall(self, external_overall):
        self.__overall = external_overall

    @property
    def avg(self):
        try:
            return (round((self.points / self.matches_played), 1))
        except:
            return 0
    
    def set_height(self):
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

    def get_competition_stats(self):
        ''' return matches_played, goals, assists, points '''
        return [ self.matches_played, self.goals, self.assists, self.points, self.id ] 

    # Gera o output pro desenvolvedor
    def __repr__(self):
        return f'Player({self.name})'

    # Gera o output para o usuario final
    def __str__(self):
        return f'Player({self.name})'

    def data(self):
        return [
            self.name, self.nationality, self.age, self.overall, self.current_club,
            self.position, self.matches_played, self.goals, self.assists, self.avg, 
            self.market_value, self.salary, self.height, self.weight, self.foot
        ]

    def increase_overall(self):
        self.__overall += 1

    def decrease_overall(self):
        self.__overall -= 1
