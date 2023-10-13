from collections import defaultdict

def retuns_logs(stats: dict, scoreboard: str, home_goal: int, away_goal: int) -> dict:
    ''' Return a dict with the game logs '''

    return {
        "game_stats": stats,
        "scoreboard": scoreboard,
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
            "home_goals": home_goal,
            "away_goals": away_goal                
        }
    }

def def_stats(home_team: str, away_team: str) -> dict:
    return {
    home_team: {
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
    away_team: {
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