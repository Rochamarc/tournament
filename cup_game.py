from classes.club import Club
from classes.player import Player
from classes.stadium import Stadium
from game import Game 

from random import choice

# TODO  1- adicionar um sistema de penaltis
#       2- adicisionar penaltis nos logs
#       3- declarar um vencedor caso vá aos penaltis
#       4- modificar a base de dados para se adequar ao novo sistema
#       


class CupGame(Game):
    """
    """
    
    def __init__(self, home: Club, away: Club, competition: str, competition_id: int, 
                 season: str, phase: str, game_number: int, stadium: Stadium, 
                 first_leg_home_goals: int=0, first_leg_away_goals: int=0, 
                 match_round: int=0, ticket: int=50):
        
        # Instantiate Game variables
        super().__init__(home, away, competition, competition_id ,season, match_round, stadium, ticket)
        self.phase = phase        
        self.game_number = game_number

        # this is for the NOW home and away clubs, not the home and away from database
        # this has to be inverted in the class instance outside, the code doesnt have
        # a method that handles this
        self.first_leg_home_goals = first_leg_home_goals
        self.first_leg_away_goals = first_leg_away_goals

        self.logs['game_info']['phase'] = self.phase 
        self.logs['game_info']['game_number'] = self.game_number

        # update first leg goals
        if self.game_number == 2:
            self.add_first_leg_goals(first_leg_home_goals, first_leg_away_goals)

    
    def start(self) -> dict:
        """Initialize a match start

        Returns
        -------
            A dict with all the game stats, movements & information
        """

        # subscribe the method of game to adapt the new features that only cup have


        time = 0
        move_info = self.move(self.home, self.away, 'middle')

        while time < 90:
            # This is the ninety minutes simulation part 
            if self.home_goal == 7 or self.away_goal == 7 : break 
            move_info = self.move(move_info['club_possession'], move_info['other_club'], move_info['field_part'], move_info['sender'])
            
            # make the game have more passes
            if not move_info['keep_ball_possession'] : time += 1

        # update logs numbers
        self.update_scoreboard_on_logs()
        self.update_goals_on_logs()
        self.update_winner_on_logs()

        if self.game_number == 2:
            winner = self.check_winner()
            
            if not winner:
                self.penalty_shootout()
            
            self.update_penalties_on_logs()
            self.update_winner_by_penalties_on_logs()
        
        return self.logs 
    
    def check_winner(self) -> bool:
        """
        """
        
        home_goals = self.home_goal + self.first_leg_home_goals
        away_goals = self.away_goal + self.first_leg_away_goals

        if home_goals == away_goals:
            return False
        
        self.update_winner_on_logs()
        return True

    def add_first_leg_goals(self, home_goals: int, away_goals: int) -> None:
        """
        """
    
        self.logs['game_info']['first_leg_home_goals'] = home_goals
        self.logs['game_info']['first_leg_away_goals'] = away_goals

    def penalty_shootout(self) -> None:
        """Simulates a panlty shootout 5 alternate penalties for each club.
        if tie, the run one shoot until one of the club misses and the other get it right
        
        Returns
        -------
            None
        """

        home_shooters = self.home_players.copy()
        away_shooters = self.away_players.copy()

        home_keeper = self.select_player(self.home, 'goalkeeper')
        away_keeper = self.select_player(self.away, 'goalkeeper')

        for i in range(5):
            # five penalties per club
            # each iterable is a shoot for each team
            home_shooter = home_shooters.pop()
            away_shooter = away_shooters.pop()

            
            if self.penalty_shooting(home_shooter, away_keeper):
                self.home_penalties += 1
                        
            if self.penalty_shooting(away_shooter, home_keeper):
                self.away_penalties += 1
        
        # alternate penalties
        if self.home_penalties == self.away_penalties:
            home = 0
            away = 0

            while home == away:
                
                if len(home_shooters) == 0:
                    home_shooters = self.home_players.copy()
                    away_shooters = self.away_players.copy()

                home_shooter = home_shooters.pop()
                away_shooter = away_shooters.pop()
                
                if self.penalty_shooting(home_shooter, away_keeper):
                    home += 1
                            
                if self.penalty_shooting(away_shooter, home_keeper):
                    away += 1

                
                self.home_penalties += home
                self.away_penalties += away
        
        return None

    def penalty_shooting(self, shooter: Player, keeper: Player) -> bool:
        """Simulate a penalty shoot

        Parameters
        ----------
        shooter : Player
            Player object shooting the penalty
        keeper : Player
            Player object defending the penalty

        Returns
        -------
            A bool for shooter & keeper decision using AND operator
        """
        return self.decision(shooter.overall) and self.decision(keeper.overall, num_trials=3)

    def check_penalties_winner(self) -> Club:
        """
        """
        if self.home_penalties > self.away_penalties:
            return self.home
        return self.away    

if __name__ == "__main__":
    CupGame()