from collections import defaultdict
from random import choice, randint 
from base_game import BaseGame
from classes.player import Player 

class Game(BaseGame):
    def __init__(self, home, away, competition, season, match_round, stadium, ticket=50):
        super().__init__(home, away, season, stadium, ticket)

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

        self.add_players_on_logs()

    def start(self) -> dict:
        ''' Initialize a match, return the game logs '''

        time = 0
        move_info = self.move(self.home, self.away, 'middle')

        while time < 90:
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
        
        defensor = self.select_player_on_field(defense_club, field_part)
        sender = None
        
        # will generate all the block code of substition
        self.check_for_sub_club(attack_club)

        club_possession = None
        other_club = None
        
        destiny = choice(['back', 'middle', 'front'])
        
        player_decision = self.player_decision(field_part) 

        if player_decision == 'keep_ball_possession':
            # Keep ball possession
            # send to another player and keep the field
            
            attack_move = 'pass'
            field_part = field_part
            sender = self.select_player_on_field(attack_club, field_part)

            if not self.move_decision(attacker, defensor):
                # not sucessfull pass
                # keep the field part and invert the ball possession

                club_possession, other_club = defense_club, attack_club
                sender = defensor
            
            club_possession, other_club = attack_club, defense_club

        
        elif player_decision == 'advance':
            # Make an attack move

            if field_part == 'back':
                destiny = choice(['middle','front'])
            else:
                destiny = 'front'
            
            attack_move = choice(['pass','projection'])
            sender = self.select_player_on_field(attack_club, destiny)

            if not self.move_decision(attacker, defensor):
                # failed pass or projection

                if defense_move == 'tackle':
                    ''' Tackle '''
                    self.update_player_stats_on_logs('tackles', defensor)
                    self.update_game_stats_on_logs('tackles', defense_club.name)

                elif defense_move == 'ball_steal': 
                    ''' Ball steal '''              
                    self.update_player_stats_on_logs('stolen_balls', defensor)
                    self.update_game_stats_on_logs('stolen_balls', defense_club.name)

                club_possession, other_club = defense_club, attack_club
                sender = defensor 
            else:
                # sucessfull pass or projection 
                # change the field_part to destiny
                # doesnt change the sender
                # TODO add a pass to logs and database

                field_part = destiny
                club_possession, other_club = attack_club, defense_club
                
        
        else:
            # take_a_risk
            keeper = self.select_player(defense_club, 'goalkeeper')
            attack_move = 'finish'

            # i can decrease the attacker chance based on the part of the field 
            # that he is shooting passing a decrease_attacker_chance = 0 and adding
            # to the value of the attacker decision 
            if not self.move_decision(attacker, keeper):
                ''' Defense '''

                field_part = 'back'
                sender = keeper 

                self.update_player_stats_on_logs('defenses', keeper)                
                self.update_game_stats_on_logs('saves', defense_club.name)
            
            else:
                ''' goal '''
                
                field_part = 'middle'

                midfielder =  self.select_player(attack_club, 'midfielder')
                self.finish(midfielder, attacker, attack_club)
                
                # change sender to defensor
                sender = self.select_player(defense_club, 'attacker') 

            # no matter what happen above,
            # this block always represents a shot on target
            self.update_game_stats_on_logs('shots on target', attack_club.name)
            club_possession, other_club = defense_club, attack_club
                
        
        move_info['field_part'] = field_part
        move_info['club_possession'] = club_possession
        move_info['other_club'] = other_club
        move_info['sender'] = sender

        return move_info
    
    def player_decision(self, field_part=None) -> str:
        ''' Return a decision that can be made by a player '''
        if field_part == 'front':
            return choice(['keep_ball_possesion', 'take_a_risk'])
        return choice(['keep_ball_possession', 'advance', 'take_a_risk'])

    def move_decision(self, attacker, defensor) -> bool:
        ''' Based on attacker and defensor overall make a decision, but the defensor have advantage '''
        return not self.decision(defensor.overall) and self.decision(attacker.overall)  

    def select_player_on_field(self, club, field_part: str):
        ''' Return a player based on field part '''
        return self.select_player(club, self.select_position_by_field(field_part))

    def define_defense_on_field(self) -> str:
        ''' Return a defense move based on field part '''
        return choice(['ball_steal', 'tackle'])

    def select_position_by_field(self, field_part: str) -> str:
        ''' Return a position based on the field_part argument '''

        if field_part == 'back':
            return 'attacker'
        if field_part == 'middle':
            return 'midfielder'
        
        return 'defender'

    def define_attack_on_field(self, field_part: str) -> str:
        ''' Return attack move based on field part ''' 
        if field_part == 'front':
            return choice(['pass', 'finish'])
        return choice(['pass', 'projection'])

    def select_player(self, club, player_position):
        ''' Return a player from the club start eleven '''

        if club == self.home:
            start_eleven = self.home_players
        elif club == self.away:
            start_eleven = self.away_players 
        else:
            raise NameError('Club {} does not match {} or {}'.format(club, self.home.name, self.away.name))

        if player_position == 'any':
            return choice(start_eleven)

        player = choice([player for player in start_eleven if player.position in self.positions[player_position]])

        return player 

    def penalty(self, keeper, attacker, club_finish) -> bool:
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
            self.update_game_stats_on_logs('shots on target', club_finish.name)

            return False
        
        self.add_a_goal(club_finish, attacker)

        # update the game_stats & player_stats on logs
        self.update_game_stats_on_logs('goals', club_finish.name)
        self.update_player_stats_on_logs('goals', attacker)

        return True

    def finish(self, midfielder, attacker, club_finish):
        ''' Represents a sucessfull finish. Update the stats on logs '''

        assist = choice([True,False]) # defines if the goal have an assist

        self.add_a_goal(club_finish, attacker)

        # Add stats to logs
        self.logs['game_stats'][club_finish.name]['goals'] += 1
        self.logs['player_stats']['goals'][attacker] += 1

        if assist : self.logs['player_stats']['assists'][midfielder] += 1 

        return True
    
    def subs(self, club) -> bool:
        ''' Will make a sub if everything goes well return True '''

        # Defines s_check, startin, bench, n_subs
        sub_opt = self.sub_options(club) 
        s_check, starting = sub_opt[0], sub_opt[1]
        bench, home_away = sub_opt[2], sub_opt[3]
        
        # Select the player that is going to leave
        player_out = choice(starting) 

        # Select the possible players based on the position
        options = self.set_options(player_out.position, bench)
        
        if s_check and options:
            # Select player the will enter the field
            player_in = choice(options) 
            
            # Remove subed player from starting eleven & bench
            starting.remove(player_out) 
            bench.remove(player_in) 
            
            # Add player to starting eleven
            starting.append(player_in) 
            
            # Remove one from subb
            self.remove_one_sub(club)
            
            # add player_in on the logs
            self.add_player_on_logs(home_away, player_in)
            
            return True
        return False 
    
    def add_a_goal(self, club, attacker) -> None:
        if club == self.home:
            self.home_goal += 1
            self.home_player_goals[attacker] += 1
            return None 
        
        self.away_goal += 1
        self.away_player_goals[attacker] += 1
        return None

    def check_for_sub_club(self, club) -> bool:
        ''' Receive a club as argument and return true if the sub will happen '''
        sub_club = self.select_club_by_home_away(club)
        n_subs = self.select_club_number_of_subs_by_home_away(sub_club)

        if self.check_number_subs(n_subs):
            self.subs(sub_club)
            return True 
        return False 

    def check_number_subs(self, n_sub: int) -> None:
        ''' Return True or False if the n of subs is greater than 0 '''
        if n_sub > 0 :  return choice([True, False]) 
            
    def select_club_by_home_away(self, club):
        ''' Return a club pointer based on home or away '''
        return self.home if club == self.home else self.away

    def select_club_number_of_subs_by_home_away(self, club):
        ''' '''
        return self.home_subs if club == self.home else self.away_subs

    def sub_options(self, club) -> list:
        ''' Return the s_check, starting, bench & home_away '''
        if club == self.home:
            return [ self.check_subs(self.home_subs), self.home_players, self.home_bench, 'home' ]
        return [self.check_subs(self.away_subs), self.away_players, self.away_bench, 'away']

    def remove_one_sub(self, club) -> None:
        ''' Remove one sub '''
        if club == self.home : self.home_subs -= 1
        if club == self.away : self.away_subs -= 1        

    def set_options(self, player_position, bench):
        ''' Return a list of players for a position that matches the player_position '''
        
        positions = self.positions.copy()
        del positions['goalkeeper']
        
        for key, item in positions.items():
            if player_position in item:
                return [ b for b in bench if b.position in positions[key] ]
        return None
    
    def decision(self, p_overall) -> bool:
        ''' Retrun True if player overall is greater then a random between (1,100) '''
        return randint(49, 100) < p_overall 

    def invert_decision(self, p_overall) -> bool:
        ''' Retrun True if player overall is smaller then a random between (1,100) '''
        return randint(49, 100) > p_overall
    
    def check_subs(self, n_subs) -> bool:
        ''' returns True if the team still have subs left '''
        return n_subs > 0

    def penal_decision(self) -> bool:
        ''' 1 of 5 chances of a penalty kick '''
        return choice([True, False, False, False, False])

    def offside(self):
        ''' 1 0f 2 chances of offside '''
        return choice([True, False])
    
    def __repr__(self) -> str:
        return 'Game({} x {})'.format(self.home, self.away)