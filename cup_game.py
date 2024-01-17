from classes.club import Club
from classes.player import Player
from classes.stadium import Stadium
from game import Game 


from decision_maker import complex_decision

class CupGame(Game):
    """Class that deals with Cup Game Simulation, generates data and makes game decisions automatically
    inherits from Game and BaseGame

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
        """Override the Game.start method, adding new rules and 
        a penalty shootout

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

        if self.game_number == 1:
            # update this on logs to the next game
            self.logs['cup_info']['first_leg_home_goals'] = self.home_goal
            self.logs['cup_info']['first_leg_away_goals'] = self.away_goal
        
        # update logs numbers
        self.update_scoreboard_on_logs()
        self.update_goals_on_logs()
        self.update_winner_on_logs()

        # here are the rules that defines if the game has penalties or not
        if self.game_number == 2:
            winner = self.check_winner()
            
            if not winner:
                self.penalty_shootout()
            
                self.update_penalties_on_logs()
                self.update_winner_by_penalties_on_logs()
            
  

        return self.logs 
    
    def check_winner(self) -> bool:
        """Check's if the game has a winner on second game

        Returns
        -------
            True if has a winner and False if it's a tie
        """
        
        home_goals = self.home_goal + self.first_leg_home_goals
        away_goals = self.away_goal + self.first_leg_away_goals

        if home_goals == away_goals:
            return False
        
        self.update_winner_on_logs()
        return True

    def add_first_leg_goals(self, home_goals: int, away_goals: int) -> None:
        """Add goals on logs

        Parameters
        ----------
        home_goals : int
            A integer value of home_goals
        away_goals : int
            A integer value of away_goals

        Returns
        -------
            None
        """
    
        self.logs['game_info']['first_leg_home_goals'] = home_goals
        self.logs['game_info']['first_leg_away_goals'] = away_goals

    def penalty_shootout(self) -> None:
        """Simulates a penalty shootout 5 alternate penalties for each club.
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
            decision between shooter and keeper
        """

        return complex_decision(shooter.overall) and complex_decision(keeper.overall)

    def check_penalties_winner(self) -> Club:
        """Check for a penalties winner

        Returns
        -------
            home if home_penalties > away_penalties or away         
        """

        if self.home_penalties > self.away_penalties:
            return self.home
        return self.away    

if __name__ == "__main__":
    CupGame()