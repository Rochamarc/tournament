from collections import defaultdict
from random import choice 

class BaseGame:
    def __init__(self) -> None:
        self.home_goal = 0
        self.away_goal = 0

        self.home_subs = 5
        self.away_subs = 5

        self.home_player_goals = defaultdict(int)
        self.away_player_goals = defaultdict(int)

        self.scoreboard = {
            'competition': self.competition,
            'season': self.season,
            'round': self.round,
            'hour': choice(['11:00', '16:00', '18:00', '19:00', '21:00']),
            'location': self.stadium.location,
            'home_club': self.home_club,
            'away_club': self.away_club,
            'conditions': f"{choice(['Cold', 'Hot'])} {choice(['Bright', 'Cloudless', 'Cloudy', 'Rainy', 'Light Rain'])}"
        }

    @property
    def stats(self) -> dict:
        return {
        "home_stats": {
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
        "away_stats": {
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