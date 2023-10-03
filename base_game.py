from collections import defaultdict
from random import choice 

# Logs will storage the game data. All info that was storage inside the class
# will now be inside the logs, and later upload to database
#
#
#
#

class BaseGame:
    def __init__(self, home_team, away_team, competition, season, m_round) -> None:
        self.home_goal = 0
        self.away_goal = 0

        self.home_subs = 5
        self.away_subs = 5

        self.home_player_goals = defaultdict(int)
        self.away_player_goals = defaultdict(int)

        self.stats = self.def_stats(home_team, away_team)

        self.scoreboard = {
            'competition': competition,
            'season': season,
            'round': m_round,
            'hour': choice(['11:00', '16:00', '18:00', '19:00', '21:00']),
            'location': self.stadium.location,
            'home_club': home_team.name,
            'away_club': away_team.name,
            'conditions': f"{choice(['Cold', 'Hot'])} {choice(['Bright', 'Cloudless', 'Cloudy', 'Rainy', 'Light Rain'])}"
        }

        self.logs = {
            "game_stats": self.stats,
            "scoreboard": self.scoreboard,
            "player_stats": {
                "assists": defaultdict(int),
                "goals": defaultdict(int),
                "tackles": defaultdict(int),
                "defenses": defaultdict(int),
                "dificult_defenses": defaultdict(int),
                "clearances": defaultdict(int),
                "fouls": defaultdict(int)
            },
            "players": {
                "home_club": [],
                "away_club": []
            },
            "others": {
                "winner": [],
                "loser": [],
                "home_goals": self.home_goal,
                "away_goals": self.away_goal                
            }
        }

    def def_stats(self, home_team, away_team) -> dict:
        return {
        home_team.name: {
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
        away_team.name: {
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
    
    def add_stats(self, team: str, move: str) -> None:
        ''' add a value to stats '''   

        self.stats[team][move] += 1 
        if move == 'shots on target' : self.stats[team]['shots'] += 1
        
        return None 