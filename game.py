from collections import defaultdict 
from random import choice, randint
from database import GameData, PlayerData

# Registrar os jogos 
#
#

game_data = GameData()
player_data = PlayerData()

class Game:
    def __init__(self, home_club, away_club, competition, m_round, season, head_stadium=None, verbose=False):
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

        self.players_out = [] # list dedicated to players the are subbed
        
        self.home_players = [ player for player in self.home_club.start_eleven ]
        self.home_bench = [ player for player in self.home_club.bench ]
        
        self.away_players = [ player for player in self.away_club.start_eleven ]
        self.away_bench = [ player for player in self.away_club.bench ]
        
        self.home_player_goals = defaultdict(int)
        self.away_player_goals = defaultdict(int)

        # Stats
        self.stats = {
            "home_stats": {
                'shots' : 0,
                'shots on target' : 0,
                'fouls' : 0,
                'tackles' : 0,
                'saves' : 0,
                'ball possession' : 0,
                'offsides' : 0,
                'free kicks' : 0
            },
            "away_stats": {
                'shots' : 0,
                'shots on target' : 0,
                'fouls' : 0,
                'tackles' : 0,
                'saves' : 0,
                'ball possession' : 0,
                'offsides' : 0,
                'free kicks' : 0
            }
        }


        self.scoreboard = {
            'competition': self.competition,
            'season': self.season,
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

        self.add_matches(self.home_players)
        self.add_points(self.home_players, 4.0)
              
        self.add_matches(self.away_players)
        self.add_points(self.away_players, 4.0)
        
        self.scoreboard['home_goal'] = self.home_goal # add to the dict
        self.scoreboard['away_goal'] = self.away_goal # add to the dict 

        self.get_score_board(end_game=True) # print the scorebaord

        return self.register_winner() 

    def game_data(self):
        score = f"{self.scoreboard['home_goal']} x {self.scoreboard['away_goal']}"
        hour = self.scoreboard['hour']


        game_info = [
            self.competition, self.season, hour, self.home_club.name, self.away_club.name, score, self.stadium.name,
            self.stats['home_stats']['shots'], self.stats['home_stats']['shots on target'], self.stats['home_stats']['fouls'], self.stats['home_stats']['tackles'], self.stats['home_stats']['saves'],
            self.stats['home_stats']['ball possession'], self.stats['home_stats']['offsides'], self.stats['home_stats']['free kicks'], self.stats['away_stats']['shots'], self.stats['away_stats']['shots on target'], 
            self.stats['away_stats']['fouls'], self.stats['away_stats']['tackles'], self.stats['away_stats']['saves'], self.stats['away_stats']['ball possession'], self.stats['away_stats']['offsides'], self.stats['away_stats']['free kicks']    
        ]
        
        return game_info

        # game_data.insert_games_db(game_info)

    @property
    def data(self):
        ''' Return the scoredboad info and game stats info '''
        # this is the api pointer to each club
        home = f"http://still-wave-44749.herokuapp.com/clubs/{self.home_club.id}/"
        visitors = f"http://still-wave-44749.herokuapp.com/clubs/{self.away_club.id}/"
        
        data = {
            'competition': self.scoreboard['competition'],
            'season': self.scoreboard['season'],
            'hour': self.scoreboard['hour'],
            'score': f"{self.scoreboard['home_goal']} x {self.scoreboard['away_goal']}",
            'stadium': self.stadium.name,
            'home_team': home,
            'away_team': visitors,
            'home_shots' : self.stats['home_stats']['shots'],
            'home_shots_on_target' : self.stats['home_stats']['shots on target'],
            'home_fouls' : self.stats['home_stats']['fouls'],
            'home_tackles' : self.stats['home_stats']['tackles'],
            'home_saves' : self.stats['home_stats']['saves'],
            'home_ball_possession' : self.stats['home_stats']['ball possession'],
            'home_offsides' : self.stats['home_stats']['offsides'],
            'home_freekicks' : self.stats['home_stats']['free kicks'],
            'away_shots' : self.stats['away_stats']['shots'],
            'away_shots_on_target' : self.stats['away_stats']['shots on target'],
            'away_fouls' : self.stats['away_stats']['fouls'],
            'away_tackles' : self.stats['away_stats']['tackles'],
            'away_saves' : self.stats['away_stats']['saves'],
            'away_ball_possession' : self.stats['away_stats']['ball possession'],
            'away_offsides' : self.stats['away_stats']['offsides'],
            'away_freekicks' : self.stats['away_stats']['free kicks']
        }


        return data

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
        '''

        ''' Add one digit to player.match and points '''
        
        time = 0
        move_info = self.move(self.home_club, self.away_club, 'middle')

        while time < 80:
            if self.home_goal == 7 or self.away_goal == 7:
                break
            move_info = self.move(move_info['club_possession'], move_info['other_club'], move_info['field_part'], move_info['sender'])
            time += 1

        self.check_game_stats() # add extra points to the players

        self.scoreboard['home_goal'] = self.home_goal 
        self.scoreboard['away_goal'] = self.away_goal  
        self.scoreboard['home_player_goals'] = self.home_player_goals
        self.scoreboard['away_player_goals'] = self.away_player_goals

        return True 

    def move(self, attack_club, defense_club, field_part, sender=None):
        '''
            {
                'destiny': ''
                'club_possession': ''
                'other_club': ''
                'sender': ''
                
            }
        '''

        move_info = {}

        
        attacker = self.select_player(attack_club, 'any') # select any player                

        if sender:
            attacker = sender # select any player                


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

        club_possession = None
        other_club = None
        attack_move = None
        sender = None
        destiny = None
        attack_move_sucess = None
        defense_move = None
        defensor = None
        defense_move_sucess = None

        if field_part == 'back':
            attack_move = choice(['pass', 'projection'])
            destiny = choice(['back', 'middle', 'front'])
            attack_move_sucess = self.decision(attacker.overall)

            defense_move = choice(['interception', 'tackle'])
            defensor = self.select_player(defense_club, 'attacker')
            defense_move_sucess = self.decision(defensor.overall)


        elif field_part == 'middle':
            attack_move = choice(['pass', 'projection'])
            destiny = choice(['back', 'middle', 'front'])
            attack_move_sucess = self.decision(attacker.overall)

            defense_move = choice(['interception', 'tackle'])
            defensor = self.select_player(defense_club, 'midfielder')
            defense_move_sucess = self.decision(defensor.overall)

        elif field_part == 'front':
            attack_move = choice(['pass', 'finish'])
            destiny = choice(['back', 'middle', 'front'])
            attack_move_sucess = self.decision(attacker.overall)

            defense_move = choice(['interception', 'tackle']) 
            defensor = self.select_player(defense_club, 'defender')
            defense_move_sucess = self.decision(defensor.overall)
        else:
            raise NameError('Field Part doesnt match')


        if defense_move_sucess:
            field_part = field_part
            ''' Defense Sucess '''
            club_possession, other_club = defense_club, attack_club
            if defense_move == 'tackle': # tackle move
                sender = defensor
                self.add_stats(defense_club, 'tackles') # Add a tackle to the game stats
                self.add_points([defensor], 0.3)
            elif defense_move == 'interception': # interception move
                sender = defensor                
                self.add_points([defensor], 0.4)
            else:
                raise NameError('Move doesnt match')
            
            self.add_stats(defense_club, 'ball possession') 

        else:
            ''' Foul '''
            foul = self.decision(defensor.overall) # if false == foul
            
            field_part = field_part

            club_possession, other_club = attack_club, defense_club
            self.add_stats(attack_club, 'fouls') # add a foul to game stats
            self.add_stats(attack_club, 'ball possession') # add a ball possesssion to game stats
            self.add_stats(attack_club, 'free kicks') # add a free kick to the game stats
                

            '''
            I change the foul system to get by the defensor overall,
            the most overall has less chance to conveding a foul
            '''
            if not foul:
                pass
                """
                if field_part == 'front':
                    ''' Penalty kick '''
                    keeper = self.select_player(defense_club, 'goalkeeper')
                    shooter = self.select_player(attack_club, 'attacker') # select the shooter

                    goal = self.penalty(keeper, shooter, attack_club)
                    
                    self.add_stats(attack_club, 'shots on target')
                    self.add_stats(attack_club, 'ball possession') # add a ball possesssion to game stats

                    if goal:
                        field_part == 'middle'
                    else:
                        field_part == 'back'
                    
                    club_possession, other_club = defense_club, attack_club
                    """
            
            elif attack_move == 'finish':

                if attack_move_sucess:
                    ''' Defense Failed, if its a finish only the keeper can save them now '''

                    keeper = self.select_player(defense_club, 'goalkeeper')
                    keeper_sucess = self.decision(keeper.overall)
                    
                    if keeper_sucess:
                        ''' Defense of the keeper '''
                
                        field_part = 'back'
                        sender = keeper
                        self.add_stats(defense_club, 'saves')
                        self.add_stats(attack_club, 'shots on target')
                        self.defense(keeper)
                        self.add_stats(defense_club, 'ball possession') # add a ball possesssion to game stats

                    else:
                        ''' GOAL'''
                        
                        field_part = 'middle'
                        self.add_stats(attack_club, 'shots on target')
                        self.finish(keeper, defensor, self.select_player(attack_club, 'midfielder'), attacker, attack_club)
                        self.add_stats(attack_club, 'ball possession') # add a ball possesssion to game stats
                else:
                    ''' Chute pra fora '''
                
                    field_part = 'back'
                    sender = self.select_player(defense_club, 'any')
                    self.add_stats(attack_club, 'shots')
                    self.add_stats(defense_club, 'ball possession') # add a ball possesssion to game stats
                
                club_possession, other_club = defense_club, attack_club

            else:
                if attack_move_sucess:
                    ''' move success ''' 
                    club_possession, other_club = attack_club, defense_club
                    field_part = destiny
                    sender = attacker
                    self.add_stats(attack_club, 'ball possession') # add a ball possesssion to game stats
                else:
                    ''' move failed '''
                    club_possession, other_club = defense_club, attack_club
                    field_part = field_part
                    self.add_stats(defense_club, 'ball possession')

        move_info['field_part'] = field_part
        move_info['club_possession'] = club_possession
        move_info['other_club'] = other_club
        move_info['sender'] = sender

        return move_info

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

        if player_position == 'any':
            return choice(start_eleven)

        positions = {
            "goalkeeper": [ 'GK' ],
            "defender": [ 'CB', 'RB', 'LB'],
            "midfielder": [ 'DM', 'CM', 'AM'],
            "attacker": [ 'CF', 'SS', 'WG' ]
        }

        player = choice([player for player in start_eleven if player.position in positions[player_position]])

        return player 

    def penalty(self, keeper, attacker, club_finish):
        ''' Represents a penalty kick '''

        shot = self.decision(attacker.overall)
        defense = self.decision(keeper.overall)

        goal = None
        defense = None 

        if shot:
            ''' goal '''
            goal = True

        elif defense:
            ''' Defense '''
            defense = True
        else:
            ''' goal '''
            goal = True


        if defense and not goal:
            # add points to keeper
            self.add_points([keeper], 1.0)
            return False
        else:
            if club_finish == self.home_club:
                self.home_goal += 1
                self.home_player_goals[attacker] += 1 
            elif club_finish == self.away_club:
                self.away_goal += 1
                self.away_player_goals[attacker] += 1
            else:
                raise NameError("Club finish doesn't match with home or away club")

            self.add_points([attacker], 1.5)    
            self.add_goal(attacker)

            # loose points for conced a goal
            self.sub_points(keeper, 0.9)


    def defense(self, keeper):
        """ Represents a defense, will add points to goalkeeper """
        dd = choice([True, False])

        if dd:
            points = 0.8
        else:
            points = 0.4
    
        self.add_points([keeper], points)

        return True

    def finish(self, keeper, defensor, midfielder, attacker, club_finish):
        ''' Represent a gols, will add points to attacker and remove opposite 
            and register the goals and asssits inside the class
        '''
        assist = choice([True,False]) # defines if the goal have an assist

        if assist:
            ''' goal with assist '''
            self.add_points([midfielder], 1.0) # Points for assist
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

        self.add_points([attacker], 1.5)    
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
        
        self.add_points([player_in], 1.5) # add some points
        self.add_matches([player_in]) # add matches played
        
        starting.append(player_in) # into the pitch
        
        if club == self.home_club : self.home_subs -= 1
        if club == self.away_club : self.away_subs -= 1

        if self.verbose:
            print(f'{club.name}')
            print(f"In: {player_in} {player_in.position}")
            print(f"Out: {player_out} {player_in.position}")

        self.players_out.append(player_out)
        
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
                exit_string += f"{self.stats['home_stats']['shots']} SHOTS {self.stats['away_stats']['shots']}\n"
                exit_string += f"{self.stats['home_stats']['shots on target']} SHOTS ON TARGET {self.stats['away_stats']['shots on target']}\n"
                exit_string += f"{self.stats['home_stats']['fouls']} FOULS {self.stats['away_stats']['fouls']}\n"
                exit_string += f"{self.stats['home_stats']['tackles']} TACKLES {self.stats['away_stats']['tackles']}\n"
                exit_string += f"{self.stats['home_stats']['saves']} SAVES {self.stats['away_stats']['saves']}\n"
                exit_string += f"{self.stats['home_stats']['ball possession']} BALL POSSESSION {self.stats['away_stats']['ball possession']}\n"
                exit_string += f"{self.stats['home_stats']['offsides']} OFFSIDES {self.stats['away_stats']['offsides']}\n"
                exit_string += f"{self.stats['home_stats']['free kicks']} FREE KICKS {self.stats['away_stats']['free kicks']}\n"
        
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

    def check_game_stats(self):
        """ Check for clean sheets, hat tricks and update pontuation """
        h_defensors = [ player for player in self.home_players if player.position in ['GK', 'CB', 'RB', 'LB', 'DM' ]]        
        a_defensors = [ player for player in self.away_players if player.position in ['GK', 'CB', 'RB', 'LB', 'DM' ]]

        if self.home_goal == 0:
            ''' Add clean sheat points ''' 
            for _def in h_defensors : self.add_points([_def], 0.4)
        if self.away_goal == 0:
            for _def in a_defensors : self.add_points([_def], 0.4)
        
        if self.home_goal >= 3:
            ''' Extra points for hat trick '''
            for player, goals in self.home_player_goals.items():
                if goals >= 3:
                    self.add_points([player], 5.0)
        if self.away_goal >= 3:
            for player, goals in self.away_player_goals.items():
                if goals >= 3:
                    self.add_points([player], 5.0)
                
        return True 

    def add_stats(self, club, move):
        if club == self.home_club:
            self.stats['home_stats'][move] += 1
            if self.move == 'shots on targe' : self.stats['home_stats']['shots'] += 1
        elif club == self.away_club:
            self.stats['away_stats'][move] += 1
            if self.move == 'shots on targe' : self.stats['away_stats']['shots'] += 1
        else: 
            raise NameError('Club name doesnt match')

    def __str__(self):
        return f"Game({self.home_club} x {self.away_club})"
    
    def __repr__(self):
        return f"Game({self.home_club} x {self.away_club})"
        
    def check_subs(self, n_subs):
        ''' Boolean: returns True if the team still have subs left '''
        return n_subs > 0
    
    def add_points(self, players, points):
        ''' Add points to player '''
        for player in players:
            player.points += points 
    
    def sub_points(self, player, points):
        ''' Remove points to player '''
        player.points -= points 

    def add_matches(self, players):
        ''' Add one match to player '''
        for player in players:
            player.matches_played += 1
    
    def add_goal(self, player):
        ''' Add one goal to player '''
        player.goals += 1

    def add_assist(self, player):
        ''' Add one assist to player '''
        player.assists += 1

    def update_players_match_stats(self):
        for player in self.home_players:
            player_stats = player.get_competition_stats()
            player_data.update_player_stats(player_stats)
        for player in self.away_players:
            player_stats = player.get_competition_stats()
            player_data.update_player_stats(player_stats)
        for player in self.players_out:
            player_stats = player.get_competition_stats()
            player_data.update_player_stats(player_stats)