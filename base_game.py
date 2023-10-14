from collections import defaultdict


class BaseGame:
    def __init__(self, home, away):
        ''' This will handle all that code that have to do with the game data '''

        self.stats = {
            home.name: {
                'home': True,
                'goals': 0,
                'shots' : 0,
                'shots on target' : 0,
                'fouls' : 0,
                'tackles' : 0,
                'saves' : 0,
                'ball possession' : 0,
                'offsides' : 0,
                'free kicks' : 0,
                'penalties': 0
                },
            away.name: {
                'home': False,
                'goals': 0,
                'shots' : 0,
                'shots on target' : 0,
                'fouls' : 0,
                'tackles' : 0,
                'saves' : 0,
                'ball possession' : 0,
                'offsides' : 0,
                'free kicks' : 0,
                'penalties': 0
                }
        }

        self.logs = {
            "game_stats": self.stats,
            "scoreboard": '',
            "player_stats": {
                "assists": defaultdict(int),
                "goals": defaultdict(int),
                "tackles": defaultdict(int),
                "defenses": defaultdict(int),
                "dificult_defenses": defaultdict(int),
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
            }
        }

    
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
