import numpy as np
from random import choice, randint

from base_game import BaseGame

# Nessa versão a classe nao vai guardar ou adicionar pontos ao jogadores
# ela não tem mais essa autonomia, basicamente vai computar os acontecimentos
# nos stats que estão no base_game, e vai guardar um outro dicionario que 
# cataloga a ação, o numero de ações a um determinado jogador.
#
# A ideia aqui, é que o que o jogo antes fazia ele não faz mais. Sua autonomia
# está em somente simular uma partida, não em atribuir pontos ou em modificar seja de qualquer
# maneira a partida, a essa autonomia está o base game.
# 
# Será retirada tambem toda a parte de manipulação de sting, é muita função pra
# uma só classe
# 
# A ideia aqui, é que a classe simule e retorno um enorme dicionario repleto de informação
# que será separado e upado para suas determinadas tabelas no banco de dados.

class Game(BaseGame):
    def __init__(self, home_club, away_club, competition, m_round, season, head_stadium=None):
        super().__init__(home_club, away_club, competition, season, m_round)
        self.home_club = home_club 
        self.away_club = away_club
        self.competition = competition 
        self.round = m_round
        self.season = season
        
        self.head_stadium = head_stadium

        self.players_out = [] # list dedicated to players the are subbed
        
        self.home_players = np.array([ player for player in self.home_club.start_eleven ])
        self.home_bench = np.array([ player for player in self.home_club.bench ])
        
        self.away_players = np.array([ player for player in self.away_club.start_eleven ])
        self.away_bench = np.array([ player for player in self.away_club.bench ])

    
    def start(self):
        ''' Simultes a match 
        '''
        
        self.get_score_board() 

        self.actions() # start match 

        self.home_goal = self.scoreboard['home_goal']
        self.away_goal = self.scoreboard['away_goal']

        self.scoreboard['home_goal'] = self.home_goal 
        self.scoreboard['away_goal'] = self.away_goal 

        self.get_score_board(end_game=True) # now this is a outside function with lots of arguments

        return self.register_winner() 

    def actions(self):
        ''' Simulates a football actions, pass, defense, tackle and goals
        '''
        
        time = 0
        move_info = self.move(self.home_club, self.away_club, 'middle')

        while time < 80:
            ''' This is the ninety minutes simulation part '''
            if self.home_goal == 7 or self.away_goal == 7:
                break # games cant have more than 7 goals
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
                self.add_stats(defense_club, 'tackles') # Add a tackle to the game stats
            elif defense_move == 'interception': # interception move
                sender = defensor                
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
            "midfielder": [ 'DM', 'CM', 'AM', 'LM', 'RM'],
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
 
            self.add_goal(attacker)

            # loose points for conced a goal


    def defense(self, keeper):
        """ Old:
            Represents a defense, will add points to goalkeeper 
            
            New:
            this will add a dificult defense in a dictionary with the id of the keeper
        """
        dd = choice([True, False])
        pass 

        return True

    def finish(self, keeper, defensor, midfielder, attacker, club_finish):
        ''' Represent a gols, will add points to attacker and remove opposite 
            and register the goals and asssits inside the class
        '''
        assist = choice([True,False]) # defines if the goal have an assist

        if assist:
            ''' goal with assist '''
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

        self.add_goal(attacker)
        
        return True

    def subs(self, club):
        ''' Will make a sub if everything goes well return True '''

        # Defines s_check, startin, bench, n_subs 
        if club == self.home_club:
            s_check = self.check_subs(self.home_subs)
            starting = self.home_players
            bench = self.home_bench
        elif club == self.away_club:
            s_check = self.check_subs(self.away_subs)
            starting = self.away_players
            bench = self.away_bench
        else:
            raise NameError('Club not match home_team.name or away_team.name')

        player_out = choice(starting) # Select the player that is going to leave


        options = self.set_options(player_out.position, bench) # Select the possible players based on the position
        
        if not s_check or not options:
            return False 

        player_in = choice(options) # select the player
        
        starting = np.delete(starting, np.where(starting==player_out)) # out of the field
        bench = np.delete(bench, np.where(bench==player_in)) # out of the bench
        
        self.add_matches([player_in]) # add matches played
        
        starting = np.append(starting, player_in) # into the pitch
        
        if club == self.home_club : self.home_subs -= 1
        if club == self.away_club : self.away_subs -= 1

        ''' this can go to logs, but its not decided yet
            print(f'{club.name}')
            print(f"In: {player_in} {player_in.position}")
            print(f"Out: {player_out} {player_in.position}")
        '''
        
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
        return None

    def __str__(self):
        return f"Game({self.home_club} x {self.away_club})"
    
    def __repr__(self):
        return f"Game({self.home_club} x {self.away_club})"

    def decision(self, p_overall):
        return randint(1,100) < p_overall 
    
    def check_subs(self, n_subs):
        ''' Boolean: returns True if the team still have subs left '''
        return n_subs > 0
    