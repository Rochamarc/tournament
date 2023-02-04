from classes.player import Player

from random import choice, randint, triangular

class Club:

    def __init__(self,name,country,club_class,state=None):
        self.id = None
        self.__name = name
        self.__country = country
        self.__short_country = self.country[:3].upper()
        self.__state = state
        self.club_class = club_class
        self.ranking_points = 0
        self.min_coeff = 0
        self.max_coeff = 0
        
        self.coeff = 0

        self.total_budget = self.generate_budget()
        self.salary_budget = randint(self.total_budget//2, self.total_budget)

        # The next attr are refering to handle the squad
        self.formation = "None"
        self.start_eleven = []
        self.bench = []

        self.stadium = None 

        self.generate_coeff()

    def __repr__(self):
        return f"Club({self.name})"
    
    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def short_country(self):
        return self.__short_country

    @property
    def state(self):
        return self.__state

    @property
    def overall(self):
        ''' Define the club overall on the average of player overall '''
        players = sum([ player.overall for player in self.start_eleven ] + [ player.overall for player in self.bench ]) 
        return ( players / len(players) ) 
  
    def data(self, api=True):
        ''' Return a list with name, country, state, coeff, club_class '''
        return {
            "name": self.name,
            "country": self.country,
            "state": self.state,
            "coeff": self.coeff,
            "formation": self.formation,
            "total_budget": self.total_budget,
            "salary_budget": self.salary_budget
        } if api else [ self.name, self.country, self.state, self.coeff, self.club_class, self.formation, self.total_budget, self.salary_budget ]

    def set_formation(self, players_list):
        ''' Receive a list of players 

            id | name | nationality | age | overall | club | position | matches_played | goals | assists | points | avg | 
        '''

        squad = []

        for player in players_list:
            ''' Reinstance the player data to objects '''
            p_id = player[0]
            name = player[1]
            nation = player[2]
            age = player[3]
            overall = player[4]
            club = player[5]
            posi = player[6]
            p = Player(name, nation, age, posi, 0, 100, current_club=club)
            p.id = p_id
            p.insert_overall(overall)
            squad.append(p)
        
        squad.sort(key=lambda player : player.overall) # Sorting items by overall not reverse

        self.formation : self.formation = choice(['3-5-2', '4-3-3', '4-4-2']) # set formation if false

        keepers = [ player for player in squad if player.position == 'GK' ]
        backs = [ player for player in squad if player.position in ['CB','RB','LB'] ]
        midfielders = [ player for player in squad if player.position in ['DM','CM','AM'] ]
        attackers = [ player for player in squad if player.position in ['CF','SS','WG'] ]

        forma = [ int(i) for i in self.formation.replace('-', ' ').split(' ') ]
            
        self.start_eleven.append(keepers.pop())

        for _ in range(forma[0]):
            self.start_eleven.append(backs.pop())
        for _ in range(forma[1]):
            self.start_eleven.append(midfielders.pop())
        for _ in range(forma[2]):
            self.start_eleven.append(attackers.pop())
        

        self.bench.append(keepers.pop())
        for i in range(2):
            self.bench.append(backs.pop())
            self.bench.append(midfielders.pop())
            self.bench.append(attackers.pop())

    def generate_budget(self):
        if self.club_class == "A":
            return randint(50_000_000, 100_000_000)
        elif self.club_class == "B":
            return randint(1_000_000, 40_000_000)
        elif self.club_class == "C":
            return randint(500_000, 900_000)
        elif self.club_class == "D":
            return randint(100_000, 450_000)

    def generate_coeff(self):
        if self.club_class == 'D':
            self.min_coeff = 50
            self.max_coeff = 60
        elif self.club_class == 'C':
            self.min_coeff = 60
            self.max_coeff = 70
        elif self.club_class == 'B':
            self.min_coeff = 70
            self.max_coeff = 75
        elif self.club_class == 'A':
            self.min_coeff = 75
            self.max_coeff = 90
        else:
            raise NameError(self.club_class, " doesnt match!")        
        
        self.coeff = randint(self.min_coeff, self.max_coeff)
        return True 

