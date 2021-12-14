from collections import defaultdict 
from random import choice
# from sqlite3.dbapi2 import register_adapter 
from classes import *
from database import GameData, PlayerData

# Registrar os jogos 
#
#

game_data = GameData()
player_data = PlayerData()

class Game:
    def __init__(self, home_club, away_club, competition, m_round, season, head_stadium=None, verbose=True):
        self.home_club = home_club 
        self.away_club = away_club
        self.competition = competition 
        self.round = m_round
        self.season = season
        if head_stadium:
            self.stadium = head_stadium
        else:
            self.stadium = self.home_club.stadium 
        self.home_goal = 0
        self.away_goal = 0

        self.home_subs = 3
        self.away_subs = 3
        
        self.home_players = [ player for player in self.home_club.start_eleven ]
        self.home_bench = [ player for player in self.home_club.bench ]
        
        self.away_players = [ player for player in self.away_club.start_eleven ]
        self.away_bench = [ player for player in self.away_club.bench ]
        
        self.home_player_goals = defaultdict(int)
        self.away_player_goals = defaultdict(int)

        # Stats
        self.home_shots = 0
        self.home_shots_on_target = 0
        self.home_fouls = 0
        self.home_tackles = 0
        self.home_saves = 0
        self.home_ball_possesion = 0
        self.home_offsides = 0
        self.home_free_kicks = 0

        self.away_shots = 0
        self.away_shots_on_target = 0
        self.away_fouls = 0
        self.away_tackles = 0
        self.away_saves = 0
        self.away_ball_possesion = 0
        self.away_offsides = 0
        self.away_free_kicks = 0

        self.scoreboard = {
            'competition': self.competition,
            'round': self.round,
            'hour': choice(['19:00', '21:00', '23:00']),
            'location': self.stadium.location,
            'home_club': self.home_club,
            'away_club': self.away_club,
            'conditions': f"{choice(['Frio', 'Calor', 'Ambiente'])} {choice(['Limpo', 'Nublado', 'Chuvoso'])}"
        }

        self.verbose = verbose
    
    def start(self):
        ''' Simultes a match 
        '''
        
        if self.verbose : self.get_score_board() # print the scoreboard

        self.actions() # start match 

        self.home_goal = self.scoreboard['home_goal']
        self.away_goal = self.scoreboard['away_goal']


        self.scoreboard['home_goal'] = self.home_goal # add to the dict
        self.scoreboard['away_goal'] = self.away_goal # add to the dict 

        self.get_score_board(end_game=True) # print the scorebaord

        return self.register_winner() 

    def save_game_database(self):
        # variables
        score = f"{self.scoreboard['home_goal']} x {self.scoreboard['away_goal']}"
        hour = self.scoreboard['hour']


        game_info = [
            self.competition, self.season, hour, self.home_club.name, self.away_club.name, score, self.stadium.name,
            self.home_shots, self.home_shots_on_target, self.home_fouls, self.home_tackles, self.home_saves,
            self.home_ball_possesion, self.home_offsides, self.home_free_kicks, self.away_shots, self.away_shots_on_target, 
            self.away_fouls, self.away_tackles, self.away_saves, self.away_ball_possesion, self.away_offsides, self.away_free_kicks    
        ]
        
        game_data.insert_games_db(game_info)

    def register_winner(self):
        ''' 
            Following the database needs, will return a dict
            {
                home_team: [ won, draw, lost, goal_f, goal_a, goal_diff, points, club_name ],
                away_team: [ ... ]
            }
        '''
        
        register = {
            'home_team': [],
            'away_team': []
        }

        if self.home_goal == self.away_goal:
            register['home_team'] = [0, 1, 0, self.home_goal, self.away_goal, (self.home_goal - self.away_goal), 1, self.home_club.name ]
            register['away_team'] = [0, 1, 0, self.away_goal, self.home_goal, (self.away_goal - self.home_goal), 1, self.away_club.name ]
        elif self.home_goal > self.away_goal:
            register['home_team'] = [1, 0, 0, self.home_goal, self.away_goal, (self.home_goal - self.away_goal), 3, self.home_club.name ]
            register['away_team'] = [0, 0, 1, self.away_goal, self.home_goal, (self.away_goal - self.home_goal), 0, self.away_club.name ]
        else:
            register['home_team'] = [0, 0, 1, self.home_goal, self.away_goal, (self.home_goal - self.away_goal), 0, self.home_club.name ]
            register['away_team'] = [1, 0, 0, self.away_goal, self.home_goal, (self.away_goal - self.home_goal), 3, self.away_club.name ]

        return register

    def actions(self):
        ''' Simulates a football actions, pass, defense, tackle and goals
            return a dict { 'home_goal': <class 'int'>, 'away_goal': <class 'int'> , 'home_player_goals': <class 'defaultdict'>, 'away_player_goals': <class 'defaultdict'> } 
        '''

        ''' Add one digit to player.match and points '''
        for player in self.home_players:
            self.add_matches(player)
            self.add_points(player, 4.0)
            player.points += 4.0   
        for player in self.away_players:
            self.add_matches(player)
            self.add_points(player, 4.0)

        for i in range(90):
            if i % 2 == 0:
                self.move(self.home_club, self.away_club)
            else:
                self.move(self.away_club, self.home_club)

        self.check_game_stats() # add extra points to the players

        self.scoreboard['home_goal'] = self.home_goal 
        self.scoreboard['away_goal'] = self.away_goal  
        self.scoreboard['home_player_goals'] = self.home_player_goals
        self.scoreboard['away_player_goals'] = self.away_player_goals

        return True 

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

        # Check and execute a Substitution
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
            raise NameError("Club name doesn't match")

        if tackle:
            """ clerance """
            self.add_stats(defense_club, 'tackle')
            self.add_points(defensor, 0.3)
        else:
            if touch:
                """ touch sucess """
                self.add_points(midfielder, 0.5) # sucessful pass
                finish = self.decision(attacker.overall)
                defense = self.decision(keeper.overall)
                if defense:
                    ''' shot on goal and a save '''
                    self.add_stats(defense_club, 'save')
                    self.add_stats(attack_club, 'shot on target')
                    self.defense(keeper)

                else:
                    ''' Shot not on goal'''
                    self.add_stats(attack_club, 'shot')
                    if finish:
                        ''' shot on goal and a goal'''
                        self.add_stats(attack_club, 'shot on target')
                        self.finish(keeper, defensor, midfielder, attacker, attack_club)
            
    def decision(self, p_overall):
        return randint(1,100) < p_overall 

    def select_player(self, club, player_position):
        ''' Return a player from the club start eleven '''

        if club == self.home_club:
            start_eleven = self.home_players
        elif club == self.away_club:
            start_eleven = self.away_players 
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        positions = {
            "goalkeeper": [ 'GK' ],
            "defender": [ 'CB', 'RB', 'LB'],
            "midfielder": [ 'DM', 'CM', 'AM'],
            "attacker": [ 'CF', 'SS', 'WG' ]
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
        ''' Represent a gols, will add points to attacker and remove opposite 
            and register the goals and asssits inside the class
        '''
        assist = choice([True,False]) # defines if the goal have an assist

        if assist:
            ''' goal with assist '''
            self.add_points(midfielder, 1.0) # Points for assist
            self.add_assist(midfielder) # add assist

        # register a goal inside this class
        # register a  { player : goals } on the current match
        ''' Will check if the club_finish matches home or away team
            then add the one digit to home_goal or away_goal
            and to the defaultdict(int) variable 
        '''
        if club_finish == self.home_club:
            self.home_goal += 1
            self.home_player_goals[attacker] += 1 
        elif club_finish == self.away_club:
            self.away_goal += 1
            self.away_player_goals[attacker] += 1
        else:
            raise NameError("Club finish doesn't match with home or away club")

        self.add_points(attacker, 1.5)    
        self.add_goal(attacker)

        # loose points for conced a goal
        self.sub_points(keeper, 0.9)
        self.sub_points(defensor, 0.8)
        
        return True

    def subs(self, club):
        ''' Will make a sub if everything goes well return True '''

        # Defines s_check, startin, bench, n_subs 
        if club == self.home_club:
            s_check = self.check_subs(self.home_subs)
            starting = self.home_players
            bench = self.home_bench
            n_subs = self.home_subs
        elif club == self.away_club:
            s_check = self.check_subs(self.away_subs)
            starting = self.away_players
            bench = self.away_bench
            n_subs = self.away_subs
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        player_out = choice(starting) # Select the player that is going to leave

        options = self.set_options(player_out.position, bench) # Select the possible players based on the position
        
        if not s_check or not options:
            return False 

        player_in = choice(options) # select the player
        
        starting.remove(player_out) # out
        bench.remove(player_in) # out from the bench
        
        self.add_points(player_in, 1.5) # add some points
        self.add_matches(player_in) # add matches played
        
        starting.append(player_in) # into the pitch
        
        if club == self.home_club : self.home_subs -= 1
        if club == self.away_club : self.away_subs -= 1

        if self.verbose:
            print(f'{club.name}')
            print(f"In: {player_in} {player_in.position}")
            print(f"Out: {player_out} {player_in.position}")

        return True

    def set_options(self, player_position, bench):
        ''' Return a list of players for a position that matches the player_position '''
        
        positions = {
            "defenders": [ 'CB', 'RB', 'LB'],
            "midfielders": [ 'DM', 'CM', 'AM'],
            "attackers": [ 'CF', 'SS', 'WG' ]
        }

        for key, item in positions.items():
            if player_position in item:
                return [ b for b in bench if b.position in positions[key] ]

        return False

    def get_score_board(self, end_game=False):
        
        exit_string = ""
        player_goal_string = ""

        exit_string += f"\nCompetition: {self.scoreboard['competition']}\n"
        exit_string += f"Round: {self.scoreboard['round']}\n" 
        exit_string += f"Location: {self.scoreboard['location']}\n"
        exit_string += f"Hour: {self.scoreboard['hour']}\n"
        exit_string += f"Conditions: {self.scoreboard['conditions']}\n"
        if end_game:
            print("="*80)
            exit_string += f"{self.scoreboard['home_club'].name.upper()} ({self.scoreboard['home_club'].short_country}) {self.scoreboard['home_goal']} x {self.scoreboard['away_goal']} {self.scoreboard['away_club'].name.upper()} ({self.scoreboard['away_club'].short_country})\n"
            
            ''' Stats '''
            if self.verbose:
                exit_string += f"{self.home_shots} SHOTS {self.away_shots}\n"
                exit_string += f"{self.home_shots_on_target} SHOTS ON TARGET {self.away_shots_on_target}\n"
                exit_string += f"{self.home_fouls} FOULS {self.away_fouls}\n"
                exit_string += f"{self.home_tackles} TACKLES {self.away_tackles}\n"
                exit_string += f"{self.home_saves} SAVES {self.away_saves}\n"
                exit_string += f"{self.home_ball_possesion} BALL POSSESSION {self.away_ball_possesion}\n"
                exit_string += f"{self.home_offsides} OFFSIDES {self.away_offsides}\n"
                exit_string += f"{self.home_free_kicks} FREE KICKS {self.away_free_kicks}\n"
        
        else:
            exit_string += f"{self.scoreboard['home_club'].name.upper()} ({self.scoreboard['home_club'].short_country}) x {self.scoreboard['away_club'].name.upper()} ({self.scoreboard['away_club'].short_country})\n"

        print(exit_string)

        if end_game:
            ''' player_goal_string will return something like these
                    (FLU) Player(Fred) 60'
            '''
            
            for tpl in self.scoreboard['home_player_goals'].items(): 
                goal_time = "" 
                for _ in range(tpl[-1]):
                    goal_time += f"{randint(1,90)}' "
                player_goal_string += f"({self.home_club.name[0:3].upper()}) {tpl[0].name} {goal_time}\n"

            for tpl in self.scoreboard['away_player_goals'].items():
                goal_time = ""
                for _ in range(tpl[-1]):
                    goal_time += f"{randint(1,90)}' " 
                player_goal_string += f"({self.away_club.name[0:3].upper()}) {tpl[0].name} {goal_time}\n" 

            print(player_goal_string) # show the players scoreboard

            if end_game:
                if self.verbose:
                    ''' save a file with a string '''
                    with open(f'files/brasileirao/serie a/2021/{self.home_club.name} x {self.away_club.name}.txt', 'w+') as file:

                        file.write(f"{self.scoreboard['home_club'].name.upper()} ({self.scoreboard['home_club'].short_country}) x {self.scoreboard['away_club'].name.upper()} ({self.scoreboard['away_club'].short_country})\n")
                        
                        for line in exit_string:
                            file.write(line)

                        file.write('\n')
                        
                        for line in player_goal_string:
                            file.write(line)

                return True

    def check_game_stats(self):
        """ Check for clean sheets, hat tricks and update pontuation """
        h_defensors = [ player for player in self.home_players if player.position in ['GK', 'CB', 'RB', 'LB', 'DM' ]]
        h_attackers = [ player for player in self.home_players if player.position in ['CM', 'AM', 'CF', 'SS', 'WG']]
        
        a_defensors = [ player for player in self.away_players if player.position in ['GK', 'CB', 'RB', 'LB', 'DM' ]]
        a_attackers = [ player for player in self.away_players if player.position in ['CM', 'AM', 'CF', 'SS', 'WG']]

        if self.home_goal == 0:
            for _def in h_defensors : self.add_points(_def, 0.4)
        if self.away_goal == 0:
            for _def in a_defensors : self.add_points(_def, 0.4)
        
        if self.home_goal > self.away_goal:
            for player in self.home_players : self.add_points(player, 1.0) 
        elif self.home_goal < self.away_goal:
            for player in self.away_players : self.add_points(player, 1.0)
        
        if self.home_goal >= 3:
            for player, goals in self.home_player_goals.items():
                if goals >= 3:
                    self.add_points(player, 5.0)
        if self.away_goal >= 3:
            for player, goals in self.away_player_goals.items():
                if goals >= 3:
                    self.add_points(player, 5.0)
                
        return True 

    def add_stats(self, club, move):
        if club == self.home_club:
            if move == 'shot':
                self.home_shots += 1
            elif move == 'shot on target':
                self.home_shots += 1
                self.home_shots_on_target += 1
            elif move == 'tackle':
                self.home_tackles += 1
            elif move == 'save':
                self.home_saves += 1
            elif move == 'foul':
                self.home_fouls += 1
            elif move == 'offside':
                self.home_offsides += 1
            elif move == 'free kicks':
                self.home_free_kicks += 1
            else:
                raise NameError('Move doesnt match')

        elif club == self.away_club:
            if move == 'shot':
                self.away_shots += 1
            elif move == 'shot on target':
                self.away_shots += 1
                self.away_shots_on_target += 1
            elif move == 'tackle':
                self.away_tackles += 1
            elif move == 'save':
                self.away_saves += 1
            elif move == 'foul':
                self.away_fouls += 1
            elif move == 'offside':
                self.away_offsides += 1
            elif move == 'free kicks':
                self.away_free_kicks += 1
            else:
                raise NameError('Move doesnt match')

        else: 
            raise NameError('Club name doesnt match')

        
        
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