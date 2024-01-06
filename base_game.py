from collections import defaultdict
from random import choice, randint
from classes.player import Player
from classes.club import Club
from classes.stadium import Stadium

class BaseGame:
    """
    Class that deals with Game logs and all data inside the Game

    ...

    Methods
    -------
    add_players_on_logs()
        Add players to logs['players']
    add_player_on_logs(home_away: str, player: Player)
        Add one player to logs['players']
    update_goals_on_logs()
        Update logs['scoreboard']
    update_goals_on_logs()
        Update logs['others']['home_goals'] & logs['others']['away_goals']
    update_winner_on_logs()
        Calculate winner and loser OR draw
    update_player_stats_on_logs(stats: str, player: Player)
        Increase by one the player_stats on logs
    update_game_stats_on_logs(stat: str, home_away: str)
        Increase by one the game_stats on logs
    update_player_stats(stats: str, player: Player)
        Update stats item on logs
    prepare_player_data_dict(home_players: list, away_players: list)
        Prepare dict data for player stats
    """
    
    def __init__(self, home: Club, away: Club, season: str, stadium: Stadium, competition: str, competition_id: int, ticket: int):
        ''' This will handle all that code that have to do with the game data '''

        self.home_goal = 0
        self.away_goal = 0

        self.home_penalties = 0
        self.away_penalties = 0

        self.home_player_goals = defaultdict(int)
        self.away_player_goals = defaultdict(int)

        self.home_subs = 5
        self.away_subs = 5


        # define the audience with the whole stadium capacity with half of the capacity
        audience = randint((stadium.capacity // 4), stadium.capacity)
        audience_full_price = audience // 1.3
        audience_half_price = audience - audience_full_price

        stats_example = {
            'home': True,
            'goals': 0,
            'shots' : 0,
            'shots on target' : 0,
            'fouls' : 0,
            'passes': 0,
            'wrong passes': 0,
            'interceptions': 0,
            'tackles' : 0,
            'stolen_balls': 0,
            'saves' : 0,
            'ball possession' : 0,
            'offsides' : 0,
            'free kicks' : 0,
            'penalties': 0
        }

        self.stats = {
            home.name: stats_example.copy(),
            away.name: stats_example.copy()
        }

        self.logs = {
            "game_stats": self.stats,
            "scoreboard": '',
            "player_stats": {
                "assists": defaultdict(int),
                "goals": defaultdict(int),
                "tackles": defaultdict(int),
                "defenses": defaultdict(int),
                "passes": defaultdict(int),
                "wrong_passes": defaultdict(int),
                "intercepted_passes": defaultdict(int),
                "difficult_defenses": defaultdict(int),
                "clearances": defaultdict(int),
                "fouls": defaultdict(int),
                "stolen_balls": defaultdict(int)
            },
            "players": {
                "home": [],
                "away": []
            },
            "others": {
                "winner": None,
                "loser": None,
                "draw": False,
                "home_goals": 0,
                "away_goals": 0                
            },
            "field_conditions": {
                "location": "{}, {}".format(stadium.city, stadium.country),
                "stadium": stadium.name,
                "audience": audience,
                "conditions": {
                    "season": season,
                    "climate": choice(['cold','hot']),
                    "weather": choice(['rain', 'rainy', 'cloudy', 'sunny', 'cloudless', 'stuffy', 'light rain']),
                    "hour": choice(['11:00','14:00','16:00','18:00','20:00','22:00'])
                }
            },
            "finances": {
                "ticket_price": ticket,
                "ticket_half_price": ticket // 2,
                "audience_full_price": audience_full_price,
                "audience_half_price": audience_half_price
            },
            "clubs": {
                "home_id": home.id,
                "away_id": away.id,
                "home": home,
                "away": away,
            },
            "competitions": {
                "name": competition,
                "id": competition_id
            },
            "stats": self.prepare_player_data_dict(home.squad, away.squad),
            "game_info": {},
            "cup_info": {
                "first_leg_home_goals": 0,
                "first_leg_away_goals": 0
            }
        }

        # THIS CAN BE ON BASE_GAME
        self.positions = {
            "goalkeeper": [ 'GK' ],
            "defender": [ 'CB', 'RB', 'LB'],
            "midfielder": [ 'DM', 'CM', 'AM', 'LM', 'RM'],
            "attacker": [ 'CF', 'SS', 'WG' ]
        }
    
    def add_players_on_logs(self) -> None:
        """Add self.home_players & self.away_players to logs['players']

        Returns
        -------
            None
        """
        
        self.logs['players']['home'] += self.home_players
        self.logs['players']['away'] += self.away_players

    def add_player_on_logs(self, home_away: str, player: Player) -> None:
        """Add one player to logs['players']

        Parameters
        ----------
        home_away : str
            Club's name
        player : Player
            Player Object

        Returns
        -------
            None
        """

        self.logs['players'][home_away].append(player)

    def update_scoreboard_on_logs(self) -> None:
        """Update the scoreboard goals on logs['scoreboard']
        
        Returns
        -------
            None
        """
        
        self.logs['scoreboard'] = "{} x {}".format(self.home_goal, self.away_goal)
        
    def update_goals_on_logs(self) -> None:
        """Update the goals on logs['others]['home_goals'] & logs['others]['away_goals']
        
        Returns
        -------
            None
        """

        self.logs['others']['home_goals'] = self.home_goal
        self.logs['others']['away_goals'] = self.away_goal
    
    def prepare_penalties_data(self) -> list:
        """Return penalties data from self.logs

        Returns
        -------
            A list containing 1, home_penalties, away_penalties
        """
        
        if self.home_penalties or self.away_penalties:
            return [ 1, self.home_penalties, self.away_penalties ]
        return [ 0, 0, 0 ]
        
    def update_penalties_on_logs(self) -> None:
        """Update the penalties on logs['others']['home_penalties'] & logs['others']['away_penalties']
        ps: This adds two new values to dictionary, they don't have this two keys originaly
        
        Returns
        -------
            None
        """
        
        self.logs['others']['home_penalties'] = self.home_penalties
        self.logs['others']['away_penalties'] = self.away_penalties

    def update_winner_by_penalties_on_logs(self) -> None:
        """Calculate the difference between self.home_penalties & self.away_penalties then update logs winner and loser
        
        Retruns
        -------
            None
        """

        if self.home_penalties > self.away_penalties:
            self.logs['others']['winner'] = self.home 
            self.logs['others']['loser'] = self.away
            return None
        self.logs['others']['winner'] = self.away 
        self.logs['others']['loser'] = self.home 
         

    def update_winner_on_logs(self) -> None:
        """Calculate the difference between self.home_goals & self.away_goals then update logs winner and loser.
        If the diference between self.home_goals & away_goals =0, update the logs['others']['draw'] = True and end function.
        
        Returns
        -------
            None
        """
        
        if self.game_number == 2:
            tie = (self.home_goal + self.first_leg_home_goals) == (self.away_goal + self.first_leg_away_goals)
            home_winner = (self.home_goal + self.first_leg_home_goals) > (self.away_goal + self.first_leg_away_goals)
            
            if tie:
                self.logs['others']['draw'] = True 
                return None
            
            if home_winner:
                winner = self.home.name
                loser = self.away.name
            else:
                winner = self.away.name
                loser = self.home.name 
        else:
            tie = self.home_goal == self.away_goal
            home_winner = self.home_goal > self.away_goal

            if tie:
                self.logs['others']['draw'] = True 
                return None
            
            if home_winner:
                winner = self.home.name
                loser = self.away.name
            else:
                winner = self.away.name
                loser = self.home.name 

            
        self.logs['others']['winner'] = winner
        self.logs['others']['loser'] = loser
    
    def update_player_stats_on_logs(self, stats: str, player: Player):
        """Increase by one the stat on logs['player_stats'][stats][player]
        

        Parameters
        ----------
        stats : str
            The stat that will be increased
        player : str
            Player Object that will be increased

        Returns
        -------
            None
        """
        
        self.logs['player_stats'][stats][player] += 1

    def update_player_stats(self, stats: str, player: Player, n: int=1) -> None:
        """Update stats item on logs

        Parameters
        ----------
        stats : str
            A string containing stat that will be increased
            stats options => matches, goals, assists, tackles, passes, wrong_passes, intercepted_passes, clearances, stolen_balls, clean_sheets, defenses, difficult_defenses, goals_conceded     
        players : Player
            A player object 
        n: int
            Value that will be added on stats
        
        Returns
        -------
            None
        """

        self.logs['stats'][player.name][stats] += n

    def update_game_stats_on_logs(self, stat: str, club_name: str):
        """Increase by one the stat on logs['game_stats'][home_away][stats]
        stats options => goals, shots, shots on target, fouls, passes, wrong passes, interceptions, tackles, stolen_balls, saves, ball possession, offsides, free kicks, penalties
        
        Parameters
        ----------
        stat : str
            The stat that will be increased
        home_away : str
            Club's name
        
        Returns
        -------
            None
        """

        self.logs['game_stats'][club_name][stat] += 1

    def prepare_player_data_dict(self, home_players: list, away_players: list) -> dict:
        """Prepare player stats data

        Parameters
        ----------
        home_players : list
            Home Club squad
        away_players : list
            Away Club squad

        Returns
        -------
            A dict with player game data for home and away players
        """

        game_data = {
            "matches": 0,
            "shots": 0,
            "shots_on_target": 0,
            "goals": 0,
            "assists": 0,
            "fouls_committed": 0,
            "tackles": 0,
            "passes": 0,
            "wrong_passes": 0,
            "intercepted_passes": 0,
            "clearances": 0,
            "stolen_balls": 0,
            "clean_sheets": 0,
            "defenses": 0,
            "difficult_defenses": 0,
            "goals_conceded": 0,     
        }

        data = {}

        for player in home_players:
            data[player.name] = game_data.copy()
            data[player.name]['player_id'] = player.id
        
        for player in away_players:
            data[player.name] = game_data.copy()
            data[player.name]['player_id'] = player.id

        return data
    
    def check_for_clean_sheets(self) -> None:
        """Check for clean sheet and update stats for clean_sheets
        to all players on stats

        Returns
        -------
            None
        """

        home_clean = not self.away_goal
        away_clean = not self.home_goal
            
        # if the oponent doesnt score then add one clean sheet to opposite side
        if home_clean:
            for player in self.logs['players']['home']:
                self.update_player_stats('clean_sheets', player)
        
        if away_clean:
            for player in self.logs['players']['away']:
                self.update_player_stats('clean_sheets', player)
 

    def check_for_goals_conceded(self):
        """Check for goals conceded and update stats for goals_conceded
        to all players on stats
        
        Returns
        -------
            None
        """

        # if the oponent made goals then add this goals to opposite side
        if self.away_goal:
            for player in self.logs['players']['home']:
                self.update_player_stats('goals_conceded', player, n=self.away_goal)
             
        if self.home_goal:
            for player in self.logs['players']['away']:
                self.update_player_stats('goals_conceded', player, n=self.home_goal)


    def update_player_matches_on_field(self) -> None:
        """Update matches from players that enter the field on self.logs['stats']

        Returns
        -------
            None
        """

        for player in self.logs['players']['home']:
            self.update_player_stats('matches', player)

        for player in self.logs['players']['away']:
            self.update_player_stats('matches', player)
    
