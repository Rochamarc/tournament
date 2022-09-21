from random import triangular

class Club:

    def __init__(self,name,country,club_class,state=None):
        self.id = None
        self.name = name
        self.country = country
        self.short_country = self.country[:3].upper()
        self.state = state
        self.club_class = club_class
        self.ranking_points = 0
        self.min_coeff = 0
        self.max_coeff = 0
        
        self.total_budget = float("{:.2f}".format(triangular(1_000_000.00, 100_000_000.00)))
        self.salary_budget = float("{:.2f}".format(triangular(500_000.00, self.total_budget)))

        # The next attr are refering to handle the squad
        self.formation = "None"
        self.start_eleven = []
        self.bench = []

        self.stadium = None 

        self.generate_coeff()
        
    def __repr__(self):
        return f"Club({self.name})"

    @property
    def overall(self):
        ''' Define the club overall on the average of player overall '''
        players = sum([ player.overall for player in self.start_eleven ] + [ player.overall for player in self.bench ]) 
        return ( players / len(players) ) 

    @property 
    def old_data(self):
        ''' Return a list with name, country, state, coeff, club_class '''
        return [self.name, self.country, self.state, (self.min_coeff + self.max_coeff) // 2, self.club_class, self.formation, self.total_budget, self.salary_budget ]
  
    def data(self, api=True):
        ''' Return a list with name, country, state, coeff, club_class '''
        return {
            "name": self.name,
            "country": self.country,
            "state": self.state,
            "coeff": (self.min_coeff + self.max_coeff) // 2,
            "formation": self.formation,
            "total_budget": self.total_budget,
            "salary_budget": self.salary_budget
        } if api  else [ self.name, self.country, self.state, (self.min_coeff + self.max_coeff) // 2, self.club_class, self.formation, self.total_budget, self.salary_budget ]

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
            p.overall = overall
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


    def generate_coeff(self):
        minimum = 55
        maximum = 60
        
        if self.club_class == 'D':
            minimum -= 12 # 43
            maximum -= 5 # 55
        elif self.club_class == 'C':
            minimum -= 10 # 45
            maximum += 0 # 60
        elif self.club_class == 'B':
            minimum += 5 # 60
            maximum += 10 # 70
        elif self.club_class == 'A':
            minimum += 15 # 70
            maximum += 25 # 85
        else:
            raise NameError(self.club_class, " doesnt match!")        
        
        # update values
        self.min_coeff = minimum
        self.max_coeff = maximum
        return True 

