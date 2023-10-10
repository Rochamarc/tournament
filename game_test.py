from collections import defaultdict
from random import choice, randint 


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

    def start(self):
        time = 0
        move_info = self.move(self.home, self.away, 'middle')

        while time < 80:
            ''' This is the ninety minutes simulation part '''
            if self.home_goal == 7 or self.away_goal == 7 : break 
            move_info = self.move(move_info['club_possession'], move_info['other_club'], move_info['field_part'], move_info['sender'])
            time += 1
    
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

        if field_part == 'back':
            attack_move = choice(['pass', 'projection'])

            defense_move = choice(['interception', 'tackle'])
            defensor = self.select_player(defense_club, 'attacker')
            defense_move_sucess = self.decision(defensor.overall)


        elif field_part == 'middle':
            attack_move = choice(['pass', 'projection'])

            defense_move = choice(['interception', 'tackle'])
            defensor = self.select_player(defense_club, 'midfielder')
            defense_move_sucess = self.decision(defensor.overall)

        elif field_part == 'front':
            attack_move = choice(['pass', 'finish'])

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
               
            elif defense_move == 'interception': # interception move
                sender = defensor                
            else:
                raise NameError('Move doesnt match')
            
           

        else:
            ''' Foul '''
            foul = self.decision(defensor.overall) # if false == foul
            
            field_part = field_part

            club_possession, other_club = attack_club, defense_club


            '''
            I change the foul system to get by the defensor overall,
            the most overall has less chance to conveding a foul
            '''
            if not foul:
                if field_part == 'front':
                    ''' Penalty kick '''
                    keeper = self.select_player(defense_club, 'goalkeeper')
                    shooter = self.select_player(attack_club, 'attacker') # select the shooter

                    goal = self.penalty(keeper, shooter, attack_club)
 

                    if goal:
                        field_part == 'middle'
                    else:
                        field_part == 'back'
                    
                    club_possession, other_club = defense_club, attack_club
                    
            
            elif attack_move == 'finish':

                if attack_move_sucess:
                    ''' Defense Failed, if its a finish only the keeper can save them now '''

                    keeper = self.select_player(defense_club, 'goalkeeper')
                    keeper_sucess = self.decision(keeper.overall)
                    
                    if keeper_sucess:
                        ''' Defense of the keeper '''
                
                        field_part = 'back'
                        sender = keeper

                        self.defense(keeper)
                

                    else:
                        ''' GOAL'''
                        
                        field_part = 'middle'
         
                        self.finish(keeper, defensor, self.select_player(attack_club, 'midfielder'), attacker, attack_club)
     
                else:
                    ''' Chute pra fora '''
                
                    field_part = 'back'
                    sender = self.select_player(defense_club, 'any')

                
                club_possession, other_club = defense_club, attack_club

            else:
                if attack_move_sucess:
                    ''' move success ''' 
                    club_possession, other_club = attack_club, defense_club
                    field_part = destiny
                    sender = attacker
  
                else:
                    ''' move failed '''
                    club_possession, other_club = defense_club, attack_club
                    field_part = field_part
  

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
        ''' Represents a penalty kick '''

        shot = self.decision(attacker.overall)
        defense = self.decision(keeper.overall)

        goal = None
        defense = None 

        # Goal or Defense
        if defense:
            defense = True
        else:
            goal = True

        if defense and not goal: return False
        
        if club_finish == self.home:
            self.home_goal += 1
            self.home_player_goals[attacker] += 1 
        elif club_finish == self.away:
            self.away_goal += 1
            self.away_player_goals[attacker] += 1
        else:
            raise NameError("Club finish doesn't match with home or away club")

        return None    

    def defense(self, keeper):
        """ This will add a dificult defense in a dictionary with the id of the keeper """
        
        dd = choice([True, False])
        pass 

        return True

    def finish(self, keeper, defensor, midfielder, attacker, club_finish):
        ''' Represent a gols, will add points to attacker and remove opposite 
            and register the goals and asssits inside the class
        '''
        assist = choice([True,False]) # defines if the goal have an assist

        # Goal with assist
        '''
        if assist : self.add_assist(midfielder) 
        '''
        if club_finish == self.home:
            self.home_goal += 1
            self.home_player_goals[attacker] += 1 
        elif club_finish == self.away:
            self.away_goal += 1
            self.away_player_goals[attacker] += 1
        else:
            raise NameError("Club finish doesn't match with home or away club")

        return True
    
    def subs(self, club) -> bool:
        ''' Will make a sub if everything goes well return True '''

        # Defines s_check, startin, bench, n_subs 
        if club == self.home:
            s_check = self.check_subs(self.home_subs)
            starting = self.home_players
            bench = self.home_bench
        elif club == self.away:
            s_check = self.check_subs(self.away_subs)
            starting = self.away_players
            bench = self.away_bench
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
        return randint(1,100) < p_overall 
    
    def check_subs(self, n_subs) -> bool:
        ''' returns True if the team still have subs left '''
        return n_subs > 0

    def __repr__(self) -> str:
        return 'Game({} x {})'.format(self.home, self.away)

