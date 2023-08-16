from random import randint  
from ranking import *
from game import Game 
from db.game_controller import GameData
from db.player_controller import PlayerData
"""
Competicao:
Rodada:
Jogo: 
Ida: (em caso de jogo 2)
Placar: 
Gol Qualificado: (em caso de gol qualificado)
Pealtis: (em caso de penaltis)
"""

# extra_time() missing
# 
#

player_data = PlayerData()
game_data = GameData()

class KnockOutGame(Game):
    def __init__(self, home_club, away_club, competition, m_round, season, phase, head_stadium, verbose):
        super().__init__(home_club, away_club, competition, m_round, season, head_stadium=head_stadium, verbose=verbose)
    
        self.phase = phase 
        self.extra_time = False 
        self.qualified_goal = False
        self.penalties_confirmation = False
        
        self.total_home = 0
        self.total_away = 0
        
        self.f_home_goal = 0
        self.f_away_goal = 0

        self.p_home = 0
        self.p_away = 0
        
        self.winner = None 
        self.loser = None 

        self.q_score = "" # ?????
        self.scoreboard['phase'] = self.phase 

    def first_leg(self):
        self.start()
        game_data.insert_game_db(self.game_data()) # save on database this is gonna make my code slower but thats ok
        return self.second_leg()
    
    def second_leg(self):
        self.update_attr()

        # self.stadium = self.home_club.stadium

        self.start()

        self.total_home += self.home_goal 
        self.total_away += self.away_goal

        self.home_player_goals.clear()
        self.away_player_goals.clear()

        # self.check_qualified_goal() # check and if True calculates if has a qualified goal
        # self.check_extra_time() # check and simulates a extra time if True
        self.check_penalties() # check for penalties
        self.penalty_shots()

        self.scoreboard['total_home'] = self.total_home
        self.scoreboard['total_away'] = self.total_away 
        
        game_data.insert_game_db(self.game_data()) # save on database this is gonna make my code slower but thats ok

        return self.scoreboard

    def check_qualified_goal(self):        
        # QUALIFIED GOAL
        # from round_16 to semi_finals
        if self.round == 2:
            if self.total_home == self.total_away:
                """ Verify for qualified goal """
                if self.f_home_goal > self.away_goal:
                    self.qualified_goal = True 
                    self.scoreboard['winner'] = self.home_club
                    self.scoreboard['loser'] = self.away_club
                    self.scoreboard['q_score'] = f"\u0332{self.f_home_goal} - {self.f_away_goal}"
                elif self.away_goal > self.f_home_goal:
                    self.qualified_goal = True 
                    self.scoreboard['loser'] = self.home_club 
                    self.scoreboard['winner'] = self.away_club 
                    self.scoreboard['q_score'] = f"{self.home_goal} - \u0332{self.away_goal}"


    def check_winner(self):
        ''' Check for the winner club '''

        if self.total_home > self.total_away:
            self.winner = self.home_club
            self.loser = self.away_club
        else:
            self.winner = self.away_club
            self.loser = self.home_club 
        
        self.scoreboard['total_home'] = self.total_home 
        self.scoreboard['total_away'] = self.total_away
        self.scoreboard['winner'] = self.winner 
        self.scoreboard['loser'] = self.loser

        return True 
         
    def check_extra_time(self):
        # EXTRA TIME
        # only in the final match 
        if self.phase == 'Final' and not self.qualified_goal:
            
            print('Prorrogacao')
            # e_goals = self.actions()
            # self.e_home_goals += e_goals['home_goal']
            # self.e_away_goals += e_goals['away_goal']
    
    def check_penalties(self):
        # Verifica se a partida vai pros penaltis
        if self.total_home == self.total_away:
            if not self.qualified_goal:
                if self.round == 2:
                    self.penalties_confirmation = True 
        else:
            if self.round == 2:
                self.check_winner()


    def update_attr(self):
        ''' Update the attr and scoreboard dict '''

        # update class attr
        self.home_club, self.away_club = self.away_club, self.home_club # update home/away clubs
        self.total_home, self.total_away = self.away_goal, self.home_goal # in the second leg the total of goals from the pervious game are switched
        self.f_home_goal, self.f_away_goal = self.away_goal, self.home_goal # the same rule aply here
        self.home_goal, self.away_goal = 0, 0
        self.home_subs += 3
        self.away_subs += 3
        self.round = 2
        
        # update from the scoreboard dict
        self.scoreboard['home_club'], self.scoreboard['away_club'] = self.home_club, self.away_club 
        self.scoreboard['round'] = self.round 
        self.scoreboard['home_player_goals'].clear()
        self.scoreboard['away_player_goals'].clear()

        return True 

    def penalty_shots(self):
        if self.penalties_confirmation: 
            for i in range(10):
                if i % 2 == 0:
                    # penalty away
                    shot = randint(1,6)
                    defense = randint(1,5)
                    if shot != defense:
                        if shot != 6: 
                            self.p_home += 1
                else:
                    # penalty away
                    shot = randint(1,6)
                    defense = randint(1,5)
                    if shot != defense:
                        if shot != 6:
                            self.p_away += 1

            # Sudden death
            if self.p_home == self.p_away:
                while self.p_home == self.p_away:

                    shot_1 = randint(1,6)
                    defense_1 = randint(1,5)

                    if shot_1 != defense_1:
                        if shot_1 != 6:
                            self.p_home += 1

                    shot_2 = randint(1,6)
                    defense_2 = randint(1,5)

                    if shot_2 != defense_2:
                        if shot_2 != 6:
                            self.p_away += 1
            
            if self.p_home > self.p_away:
                self.winner = self.home_club
                self.loser = self.away_club 
            else:
                self.winner = self.away_club
                self.loser = self.home_club 

            self.scoreboard['p_home'] = self.p_home
            self.scoreboard['p_away'] = self.p_away 
            self.scoreboard['winner'] = self.winner 
            self.scoreboard['loser'] = self.loser 

            return True 




