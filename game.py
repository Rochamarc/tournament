from collections import defaultdict
from random import choice, randint 
from base_game import BaseGame

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

        while time < 180:
            print(time)
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
        
        defensor = self.select_player_on_field(field_part)
        sender = None
        

        # will generate all the block code of substition
        self.check_for_sub_club(attack_club)

        club_possession = None
        other_club = None
        
        destiny = choice(['back', 'middle', 'front'])
        
        # Moves
        attack_move = self.define_attack_on_field(field_part)
        defense_move = self.define_defense_on_field(field_part)

        # Sucess
        attack_move_sucess = self.decision(attacker.overall)
        defense_move_sucess = self.invert_decision(defensor.overall)

        if defense_move_sucess:
            ''' This will represent a ball steal, tackle or a defense. A defensive move that is sucessfull'''

            ''' Defense Sucess '''
            club_possession, other_club = defense_club, attack_club
            sender = defensor # defino um sender
            
            if defense_move == 'tackle':
                ''' Tackle '''
                self.update_player_stats_on_logs('tackles', defensor)
                self.update_game_stats_on_logs(defense_club.name, 'tackles')

            elif defense_move == 'ball_steal': 
                ''' Ball steal '''              
                self.update_player_stats_on_logs('stolen_balls', defensor)
            
            else:
                raise NameError('Move doesnt match')

        else:
            ''' This represents a failed defensive move '''
            
            # this has to be false to represent a foul
            foul = self.decision(defensor.overall)
            
            # here we invert the possession and the club
            club_possession, other_club = attack_club, defense_club

            # declare a keeper
            keeper = self.select_player(defense_club, 'goalkeeper')

            if foul:
                ''' This represent a foul or a penalty kick '''

                if field_part == 'front':
                    ''' Penalty kick '''

                    # select shooter    
                    shooter = self.select_player(attack_club, 'attacker') # select the shooter
                    
                    # add a penalty to game_stats logs
                    self.update_game_stats_on_logs(attack_club.name, 'penalties')

                    goal = self.penalty(keeper, shooter, attack_club)
 
                    # I THINK THAT THIS HAS TO B = INSTEAD OF ==
                    if goal:
                        field_part = 'middle'
                    else:
                        field_part = 'back'
                    
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
 
                    keeper_sucess = self.decision(keeper.overall)
                    
                    if keeper_sucess:
                        ''' Keeper's defense '''

                        field_part = 'back'
                        sender = keeper # defino um sender

                        # update defensor logs move
                        self.update_player_stats_on_logs('defenses', keeper)                
                        self.update_game_stats_on_logs(defense_club.name, 'saves')
                        self.update_game_stats_on_logs(attack_club.name, 'shots on target')
                    else:
                        ''' GOAL '''
                        
                        field_part = 'middle'
         
                        self.finish(self.select_player(attack_club, 'midfielder'), attacker, attack_club)
                        sender = attacker

                else:
                    ''' Kick Out & The keeper start the ball possession '''

                    field_part = 'back'
                    sender = keeper # defino um sender 

                    # add this move to logs
                    self.update_game_stats_on_logs(attack_club.name, 'shots')
                
                # this line of code belongs to attack_move_sucess
                # independent of attack movement, the ball possession will invert
                # after attack move
                # Invert the possesion and club 
                club_possession, other_club = defense_club, attack_club
                

            else:
                """ Attack move != 'finish'. This could be a pass or porjection """

                if attack_move_sucess:
                    ''' Sucessfull pass OR projection ''' 

                    club_possession, other_club = attack_club, defense_club
                    field_part = destiny
                    sender = attacker # defino um sender

                else:
                    ''' Wrong pass or interceptation '''

                    club_possession, other_club = defense_club, attack_club
                    sender = defensor # defino um sender

                    # This has to be updated on the logs
                    # and have to be on database pass, intercpetation
                    # & clearances. This else, could be any one of this

        move_info['field_part'] = field_part
        move_info['club_possession'] = club_possession
        move_info['other_club'] = other_club
        move_info['sender'] = sender

        return move_info
    
    def select_player_on_field(field_part: str):
        ''' Return a player based on field part '''
        if field_part == 'back':
            return self.select_player(defense_club, 'attacker')
        elif field_part == 'middle'
-           return self.select_player(defense_club, 'midfielder')
        else:
            return self.select_player(defense_club, 'defender')

    def define_defense_on_field() -> str:
        ''' Return a defense move based on field part '''
        return choice(['ball_steal', 'tackle'])


    def define_attack_on_field(field_part: str) -> str:
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
            raise NameError('Club not match home_team.name or away_team.name')

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
            self.update_game_stats_on_logs(club_finish.name, 'shots on target')

            return False
        
        self.add_a_goal(club_finish, attacker)

        # update the game_stats & player_stats on logs
        self.update_game_stats_on_logs(club_finish.name, 'goals')
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
        return choice([True, False]) if n_sub > 0
            
    def select_club_by_home_away(self, club):
        ''' Return a club pointer based on home or away '''
        return self.home if club == home else self.away

    def select_club_number_of_subs_by_home_away(self, club):
        ''' '''
        return self.home_subs if club == home else self.away_subs

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
        return randint(1,100) < p_overall 

    def invert_decision(self, p_overall) -> bool:
        ''' Retrun True if player overall is smaller then a random between (1,100) '''
        return randint(1,100) > p_overall
    
    def check_subs(self, n_subs) -> bool:
        ''' returns True if the team still have subs left '''
        return n_subs > 0

    def __repr__(self) -> str:
        return 'Game({} x {})'.format(self.home, self.away)