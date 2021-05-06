from collections import defaultdict 
from random import choice 
from classes import *


# Registrar os jogos 
#
#

class Game:
    def __init__(self, home_club, away_club, competition, m_round, head_stadium):
        self.home_club = home_club 
        self.away_club = away_club
        self.competition = competition 
        self.round = m_round
        self.stadium = head_stadium
                
        self.home_goal = 0
        self.away_goal = 0

        self.home_subs = 3
        self.away_subs = 3
        
        self.home_players = [ player for player in self.home_club.start_eleven ]
        self.home_bench = [ player for player in self.home_club.bench ]
        
        self.away_players = [ player for player in self.away_club.start_eleven ]
        self.away_bench = [ player for player in self.away_club.bench ]
        
        self.h_player_goals = defaultdict(int) 
        self.a_player_goals = defaultdict(int)
    
    def start(self):
        ''' Simultes a match 
            return a dict
        '''
        
        hour = choice(['19:00', '21:00', '19:15'])
        weather = choice(['Frio', 'Calor', 'Ambiente'])
        conditions = choice(['Limpo', 'Nublado', 'Chuvoso'])
        
        game_stats = {
            "competition": self.competition,
            "round": self.round,
            "hour": hour,
            "location": self.stadium.location,
            "home_team": self.home_club,
            "away_team": self.away_club,
            "conditions": f'{weather} {conditions}' 
        }

        
        print(f"\nCompetition: {self.competition}\nRound: {self.round}\nLocation: {game_stats['location']}\nHour: {hour}\nConditions: {game_stats['conditions']}\n{self.home_club.name.upper()} ({self.home_club.short_country}) x {self.away_club.name.upper()} ({self.away_club.short_country})\n")

        goals = self.actions() # start match 

        self.home_goal = goals['home_goal']
        self.away_goal = goals['away_goal']

        """ You only have to register their goals and theis oponent goals and the object define if its a win, lose or draw """
        self.home_club.register_game(self.home_goal, self.away_goal, 'group_stage')
        self.away_club.register_game(self.away_goal, self.home_goal, 'group_stage')

        game_stats['home_goals'] = self.home_goal # add to the dict
        game_stats['away_goals'] = self.away_goal # add to the dict 

        player_goal_string = "" 
        
        # Generate player_goal_string    
        for tpl in goals['home_player_goals'].items(): 
            goal_time = "" 
            for _ in range(tpl[-1]):
                goal_time += f"{randint(1,90)}' "
            player_goal_string += f"({self.home_club.name[0:3].upper()}) {tpl[0]} {goal_time}\n"
        
        for tpl in goals['away_player_goals'].items():
            goal_time = ""
            for _ in range(tpl[-1]):
                goal_time += f"{randint(1,90)}' " 
            player_goal_string += f"({self.away_club.name[0:3].upper()}) {tpl[0]} {goal_time}\n"

        print(f"\nRound: {self.round}\nCompetition: {self.competition}\n{self.home_club.name.upper()} ({self.home_club.short_country}) {self.home_goal} x {self.away_goal} {self.away_club.name.upper()} ({self.away_club.short_country})\n")
        print(player_goal_string)

        return game_stats

    def actions(self):
        ''' Simulates a football actions, pass, defense, tackle and goals
            return a dict { 'home_goal': <class 'int'>, 'away_goal': <class 'int'> , 'home_player_goals': <class 'defaultdict'>, 'away_player_goals': <class 'defaultdict'> } 
        '''

        for player in self.home_players:
            self.add_matches(player)
            self.add_points(player, 4.0)
            player.points += 4.0   
        for player in self.away_players:
            self.add_matches(player)
            self.add_points(player, 4.0)

        for i in range(45):
            if i % 2 == 0:
                self.move(self.home_club, self.away_club)
            else:
                self.move(self.away_club, self.home_club)

        self.check_game_stats()

        return { 'home_goal': self.home_goal, 'away_goal': self.away_goal, 'home_player_goals': self.h_player_goals, 'away_player_goals': self.a_player_goals } 

    def move(self, attack_club, defense_club):
        # defensives
        keeper = self.select_player(defense_club, 'goalkeeper')
        defensor = self.select_player(defense_club, 'defender')
        
        # attackers
        midfielder = self.select_player(attack_club, 'midfielder')
        attacker = self.select_player(attack_club, 'attacker')
        
        """ Ataque = toca + chuta """
        """ Defesa = corta + defende """
        
        touch = self.decision(midfielder.overall)
        tackle = self.decision(defensor.overall)

        if attack_club == self.home_club:
            if self.home_subs > 0: 
                sub = choice([True, False])
                if sub:
                    self.subs(self.home_club)
        elif attack_club == self.away_club:
            if self.away_subs > 0: 
                sub = choice([True, False])
                if sub:
                    self.subs(self.away_club)
        else:
            pass 

        if tackle:
            """ clerance """
            self.add_points(defensor, 0.3)
        else:
            if touch:
                """ touch sucess """
                self.add_points(midfielder, 0.5) # sucessful pass
                finish = self.decision(attacker.overall)
                defense = self.decision(keeper.overall)
                if defense:
                    self.defense(keeper)
                else:
                    if finish:
                        self.finish(keeper, defensor, midfielder, attacker, self.away_club)
        
    def decision(self, p_overall):
        return randint(1,100) < p_overall 

    def select_player(self, club, player_position):
        ''' Return a player from the club start eleven '''

        if club.name == self.home_club.name:
            start_eleven = self.home_players
        elif club.name == self.away_club.name:
            start_eleven = self.home_players 
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        positions = {
            "goalkeeper": [ 'Goalkeeper' ],
            "defender": [ 'Center Back', 'Right Back', 'Left Back'],
            "midfielder": [ 'Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder'],
            "attacker": [ 'Center Forward', 'Second Striker', 'Winger' ]
        }

        player = choice([player for player in start_eleven if player.position in positions[player_position]])

        return player 


    def defense(self, keeper):
        """ Represents a defense, will add points to goalkeeper """
        dd = choice([True, False])

        if dd:
            points = 0.8
        else:
            points = 0.4
    
        self.add_points(keeper, points)

        return True

    def finish(self, keeper, defensor, midfielder, attacker, club_finish):
        ''' Represent a gols, will add points to attacker and remove opposite '''
        assist = choice([True,False])

        if assist:
            """ goal with assist """
            self.add_points(midfielder, 1.0) # Points for assist
            self.add_assist(midfielder)

        # register a goal inside this class
        # register a  { player : goals } on the current match
        if club_finish.name == self.home_club.name:
            self.home_goal += 1
            self.h_player_goals[attacker] += 1 
        elif club_finish.name == self.away_club.name:
            self.away_goal += 1
            self.a_player_goals[attacker] += 1

        self.add_points(attacker, 1.5)    
        self.add_goal(attacker)

        # loose points for conced a goal
        self.sub_points(keeper, 0.9)
        self.sub_points(defensor, 0.8)
        
        return True

    def subs(self, club):
        ''' Will make a sub if everything goes well return True '''

        # Defines s_check, startin, bench, n_subs 
        if club.name == self.home_club.name:
            s_check = self.check_subs(self.home_subs)
            starting = self.home_players
            bench = self.home_bench
            n_subs = self.home_subs
        elif club.name == self.away_club.name:
            s_check = self.check_subs(self.away_subs)
            starting = self.away_players
            bench = self.away_bench
            n_subs = self.away_subs
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        player_out = choice(starting)

        options = self.set_options(player_out.position, bench) # return a list of players
        
        if not s_check:
            return False 
        if not options:
            return False 

        player_in = choice(options) # select the player
        
        starting.remove(player_out) # out
        bench.remove(player_in) # out from the bench
        
        self.add_points(player_in, 1.5) # add some points
        self.add_matches(player_in) # add matches played
        
        starting.append(player_in) # into the pitch
        
        if club.name == self.home_club.name : self.home_subs -= 1
        if club.name == self.away_club.name : self.away_subs -= 1

        print(f'{club.name}')
        print(f"In: {player_in} {player_in.position}")
        print(f"Out: {player_out} {player_in.position}")

        return True

    def set_options(self, player_position, bench):
        ''' Return a list of players for a position that matches the player_position '''
        
        positions = {
            "defenders": [ 'Center Back', 'Right Back', 'Left Back'],
            "midfielders": [ 'Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder'],
            "attackers": [ 'Center Forward', 'Second Striker', 'Winger' ]
        }

        for key, item in positions.items():
            if player_position in item:
                return [ b for b in bench if b.position in positions[key] ]

        return False

    def check_game_stats(self):
        """ Check for clean sheets, hat tricks and update pontuation """
        h_defensors = [ player for player in self.home_players if player.position in ['Goalkeeper', 'Center Back', 'Right Back', 'Left Back', 'Defender Midfielder' ]]
        h_attackers = [ player for player in self.home_players if player.position in ['Center Midfielder', 'Attacking Midfielder', 'Center Forward', 'Second Striker', 'Winger']]
        
        a_defensors = [ player for player in self.away_players if player.position in ['Goalkeeper', 'Center Back', 'Right Back', 'Left Back', 'Defender Midfielder' ]]
        a_attackers = [ player for player in self.away_players if player.position in ['Center Midfielder', 'Attacking Midfielder', 'Center Forward', 'Second Striker', 'Winger']]

        if self.home_goal == 0:
            for _def in h_defensors : self.add_points(_def, 0.4)
        if self.away_goal == 0:
            for _def in a_defensors : self.add_points(_def, 0.4)
        
        if self.home_goal > self.away_goal:
            for player in self.home_players : self.add_points(player, 1.0) 
        elif self.home_goal < self.away_goal:
            for player in self.away_players : self.add_points(player, 1.0)
        
        if self.home_goal >= 3:
            for player, goals in self.h_player_goals.items():
                if goals >= 3:
                    self.add_points(player, 5.0)
        if self.away_goal >= 3:
            for player, goals in self.a_player_goals.items():
                if goals >= 3:
                    self.add_points(player, 5.0)
                
        return True 

    def check_subs(self, n_subs):
        ''' Boolean: returns True if the team still have subs left '''
        return n_subs > 0
    
    def add_points(self, player, points):
        ''' Add points to player '''
        player.points += points 
    
    def sub_points(self, player, points):
        ''' Remove points to player '''
        player.points -= points 

    def add_matches(self, player):
        ''' Add one match to player '''
        player.matches_played += 1
    
    def add_goal(self, player):
        ''' Add one goal to player '''
        player.goals += 1

    def add_assist(self, player):
        ''' Add one assist to player '''
        player.assists += 1