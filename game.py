from collections import defaultdict
from random import choice, randint 
from game_helper import def_stats, retuns_logs

class Game:
    def __init__(self, home, away, competition, season, match_round, stadium):
        self.home = home 
        self.away = away 
        self.competition = competition
        self.season = season 
        self.match_round = match_round
        self.stadium = stadium

        self.home_players = self.home.start_eleven
        self.home_bench = self.home.bench

        self.away_players = self.away.start_eleven
        self.away_bench = self.away.bench

        self.home_goal = 0
        self.away_goal = 0

        self.home_player_goals = defaultdict(int)
        self.away_player_goals = defaultdict(int)

        self.home_subs = 5
        self.away_subs = 5

        ''' Here we declare de database data that will manage our code to update database '''
        self.stats = def_stats(self.home.name, self.away.name)
        self.logs = retuns_logs(self.stats, '', self.home_goal, self.away_goal)

        self.add_players_on_logs()


    def start(self) -> dict:
        ''' Initialize a match, return the game logs '''

        time = 0
        move_info = self.move(self.home, self.away, 'middle')

        while time < 80:
            ''' This is the ninety minutes simulation part '''
            if self.home_goal == 7 or self.away_goal == 7 : break 
            move_info = self.move(move_info['club_possession'], move_info['other_club'], move_info['field_part'], move_info['sender'])
            time += 1

        # update logs numbers
        self.update_scoreboard_on_logs()
        self.update_goals_on_logs()
        self.update_winner_on_logs()
        
        return self.logs 
    
    def move(self, attack_club, defense_club, field_part, sender=None):
        ''' Dict with info of move
         { 'destiny': '', 'club_possession': '', 'other_club': '', 'sender': '' }
        '''

        move_info = {}

        
        attacker = self.select_player(attack_club, 'any') # select any player                

        # Select any player
        if sender : attacker = sender                 

        # Check and execute a Substitution
        if attack_club == self.home:
            if self.home_subs > 0: 
                sub = choice([True, False])
                if sub:
                    self.subs(self.home)
        elif attack_club == self.away:
            if self.away_subs > 0: 
                sub = choice([True, False])
                if sub:
                    self.subs(self.away)
        else:
            raise NameError("Club name doesn't match")

        club_possession = None
        other_club = None
        attack_move = None
        sender = None
        destiny = choice(['back', 'middle', 'front'])
        attack_move_sucess = self.decision(attacker.overall)
        defense_move = None
        defensor = None
        defense_move_sucess = None

        # This block of ifs has a good refactoring factor
        # later this will be updated
        if field_part == 'back':
            attack_move = choice(['pass', 'projection'])

            defense_move = choice(['ball_steal', 'tackle'])
            defensor = self.select_player(defense_club, 'attacker')
            defense_move_sucess = self.decision(defensor.overall)


        elif field_part == 'middle':
            attack_move = choice(['pass', 'projection'])

            defense_move = choice(['ball_steal', 'tackle'])
            defensor = self.select_player(defense_club, 'midfielder')
            defense_move_sucess = self.decision(defensor.overall)

        elif field_part == 'front':
            attack_move = choice(['pass', 'finish'])

            defense_move = choice(['ball_steal', 'tackle']) 
            defensor = self.select_player(defense_club, 'defender')
            defense_move_sucess = self.decision(defensor.overall)
        else:
            raise NameError('Field Part doesnt match')


        if defense_move_sucess:
            ''' This will represent a ball steal, tackle or a defense. A defensive move that is sucessfull'''

            field_part = field_part
            ''' Defense Sucess '''
            club_possession, other_club = defense_club, attack_club
            
            if defense_move == 'tackle':
                ''' Tackle '''
                sender = defensor
                self.update_player_stats_on_logs('tackles', defensor)

            elif defense_move == 'ball_steal': 
                ''' Ball steal '''
                sender = defensor                
                self.update_player_stats_on_logs('stolen_balls', defensor)
            
            else:
                raise NameError('Move doesnt match')

        else:
            ''' This represents a failed defensive move '''

            field_part = field_part
            
            # this has to be false to represent a foul
            foul = self.invert_decision(defensor.overall)
            
            # here we invert the possession and the club
            club_possession, other_club = attack_club, defense_club

            if foul:
                ''' This represent a foul or a penalty kick '''

                if field_part == 'front':
                    ''' Penalty kick '''

                    # select keeper and shooter
                    keeper = self.select_player(defense_club, 'goalkeeper')
                    shooter = self.select_player(attack_club, 'attacker') # select the shooter
                    
                    # add a penalty to game_stats logs
                    self.update_game_stats_on_logs(attack_club.name, 'penalties')

                    goal = self.penalty(keeper, shooter, attack_club)
 

                    if goal:
                        field_part == 'middle'
                    else:
                        field_part == 'back'
                    
                    # Here we invert the sides again
                    club_possession, other_club = defense_club, attack_club
                    
            
            elif attack_move == 'finish':
                '''
                This is NOT a foul by the defensive club, OR a sucessfull
                defensive move. So, now it's the time to the attacking club make a 
                sucessnfull attack move. In this case, a finish
                '''

                if attack_move_sucess:
                    ''' This is the attacker and keepers duel. '''

                    keeper = self.select_player(defense_club, 'goalkeeper')
                    keeper_sucess = self.decision(keeper.overall)
                    
                    if keeper_sucess:
                        ''' Keeper's defense '''
                
                        field_part = 'back'
                        sender = keeper

                        # update defensor logs move
                        self.update_player_stats_on_logs('defenses', keeper)                
                        self.update_game_stats_on_logs(defense_club.name, 'saves')
                    else:
                        ''' GOAL '''
                        
                        field_part = 'middle'
         
                        self.finish(self.select_player(attack_club, 'midfielder'), attacker, attack_club)
                else:
                    ''' Kick Out '''
                
                    field_part = 'back'
                    sender = self.select_player(defense_club, 'any')

                    # add this move to logs
                    self.update_game_stats_on_logs(attack_club.name, 'shots')
                
                # Invert the possesion and club 
                club_possession, other_club = defense_club, attack_club

            else:
                """ Attack move != 'finish'. This could be a pass or porjection """

                if attack_move_sucess:
                    ''' Sucessfull pass OR projection ''' 
                    
                    club_possession, other_club = attack_club, defense_club
                    field_part = destiny
                    sender = attacker
  
                else:
                    ''' Wrong pass or interceptation '''

                    club_possession, other_club = defense_club, attack_club
                    field_part = field_part

                    # This has to be updated on the logs
                    # and have to be on database pass, intercpetation
                    # & clearances. This else, could be any one of this

        move_info['field_part'] = field_part
        move_info['club_possession'] = club_possession
        move_info['other_club'] = other_club
        move_info['sender'] = sender

        return move_info
    
    def select_player(self, club, player_position):
        ''' Return a player from the club start eleven '''

        if club == self.home:
            start_eleven = self.home_players
        elif club == self.away:
            start_eleven = self.away_players 
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        if player_position == 'any':
            return choice(start_eleven)

        positions = {
            "goalkeeper": [ 'GK' ],
            "defender": [ 'CB', 'RB', 'LB'],
            "midfielder": [ 'DM', 'CM', 'AM', 'LM', 'RM'],
            "attacker": [ 'CF', 'SS', 'WG' ]
        }

        player = choice([player for player in start_eleven if player.position in positions[player_position]])

        return player 

    def penalty(self, keeper, attacker, club_finish) -> None:
        ''' Represents a penalty kick, and save to the logs inside this method '''

        shot = self.decision(attacker.overall)
        defense = self.decision(keeper.overall)
        
        # Goal or Defense
        if defense:
            defense = True
        
        # defense == True OR shot = False
        # to make a goal the attacker has to have a True and a False Defense
        if defense or (not shot): 
            ''' This is a defense &/OR a miss penalty'''
            
            # save the defense on logs as a DD
            # in the future the database will have a penalty defense column
            if defense : self.update_player_stats_on_logs('dificult_defenses', keeper) 

            return False
        
        if club_finish == self.home:
            ''' Here we have a goal and add the logs '''
            self.home_goal += 1
            self.home_player_goals[attacker] += 1 
        elif club_finish == self.away:
            self.away_goal += 1
            self.away_player_goals[attacker] += 1
        else:
            raise NameError("Club finish doesn't match with home or away club")

        # update the game_stats & player_stats on logs
        self.update_game_stats_on_logs(club_finish.name, 'goals')
        self.update_player_stats_on_logs('goals', attacker)

        return None    

    def finish(self, midfielder, attacker, club_finish):
        ''' Represents a sucessfull finish. Update the stats on logs '''

        assist = choice([True,False]) # defines if the goal have an assist

        if club_finish == self.home:
            self.home_goal += 1
            self.home_player_goals[attacker] += 1 
        elif club_finish == self.away:
            self.away_goal += 1
            self.away_player_goals[attacker] += 1
        else:
            raise NameError("Club finish doesn't match with home or away club")

        # Add stats to logs
        self.logs['game_stats'][club_finish.name]['goals'] += 1
        self.logs['player_stats']['goals'][attacker] += 1

        if assist : self.logs['player_stats']['assists'][midfielder] += 1 

        return True
    
    def subs(self, club) -> bool:
        ''' Will make a sub if everything goes well return True '''

        # this is for the self.add_player_on_logs only
        home_away = ''

        # Defines s_check, startin, bench, n_subs 
        if club == self.home:
            s_check = self.check_subs(self.home_subs)
            starting = self.home_players
            bench = self.home_bench
            home_away = 'home'
        elif club == self.away:
            s_check = self.check_subs(self.away_subs)
            starting = self.away_players
            bench = self.away_bench
            home_away = 'away'
        else:
            raise NameError('Club not match home_team.name or away_team.name')
        
        # Select the player that is going to leave
        player_out = choice(starting) 

        # Select the possible players based on the position
        options = self.set_options(player_out.position, bench)
        
        if not s_check or not options:
            return False 

        # Select player the will enter the field
        player_in = choice(options) 
        
        # Remove subed player from starting eleven & bench
        starting.remove(player_out) 
        bench.remove(player_in) 
        
        # Add player to starting eleven
        starting.append(player_in) 
        
        # Remove one from subb
        if club == self.home : self.home_subs -= 1
        if club == self.away : self.away_subs -= 1
        
        # add player_in on the logs
        self.add_player_on_logs(home_away, player_in)
        
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
        return None
    
    def decision(self, p_overall) -> bool:
        ''' Retrun True if player overall is greater then a random between (1,100) '''
        return randint(1,100) < p_overall 

    def invert_decision(self, p_overall) -> bool:
        ''' Retrun True if player overall is smaller then a random between (1,100) '''
        return randint(1,100) > p_overall
    
    def check_subs(self, n_subs) -> bool:
        ''' returns True if the team still have subs left '''
        return n_subs > 0

    def __repr__(self) -> str:
        return 'Game({} x {})'.format(self.home, self.away)

    def add_players_on_logs(self) -> None:
        ''' Add the initial start eleven from both sides on logs'''
        self.logs['players']['home'] += self.home_players
        self.logs['players']['away'] += self.away_players

    def add_player_on_logs(self, home_away: str, player) -> None:
        ''' Add a player on logs {'players': 'home_or_away': [] }'''
        self.logs['players'][home_away].append(player)

    def update_scoreboard_on_logs(self) -> None:
        '''' '''
        self.logs['scoreboard'] = "{} x {}".format(self.home_goal, self.away_goal)
        
    def update_goals_on_logs(self) -> None:
        ''' Update {others : home_goals: int, away_goals: int } on logs '''
        self.logs['others']['home_goals'] = self.home_goal
        self.logs['others']['away_goals'] = self.away_goal

    def update_winner_on_logs(self) -> None:
        ''' Calculate the diff between home and away goals, and update
        logs winner and lose. Or will return a tie(draw) and update 
        the draw to True and not add any club'''
        if self.home_goal == self.away_goal:
            self.logs['others']['draw'] = True 
            return None
        
        if self.home_goal > self.away_goal:
            winner = self.home.name
            loser = self.away.name
        else:
            winner = self.away.name
            loser = self.home.name 

        self.logs['others']['winner'] = winner
        self.logs['others']['loser'] = loser
        
        return None
    
    def update_player_stats_on_logs(self, stats, player):
        ''' Add one item to the player stats that is a default dict '''
        self.logs['player_stats'][stats][player] += 1

    def update_game_stats_on_logs(self, home_away, stat):
        ''' Update a field in logs { 'game_stats': [home_away]: stat += 1 } '''
        self.logs['game_stats'][home_away][stat] += 1
