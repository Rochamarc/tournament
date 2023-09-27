from random import randint


def get_scoreboard(home_club:str, away_club: str, scoreboard: dict, stats: dict, end_game=False, verbose=False) -> str:
    exit_string = ""
    player_goal_string = ""

    exit_string += f"\nCompetition:\t {scoreboard['competition']}\n"
    exit_string += f"Round:\t\t {scoreboard['round']}\n" 
    exit_string += f"Location:\t {scoreboard['location']}\n"
    exit_string += f"Hour:\t\t {scoreboard['hour']}\n"
    exit_string += f"Conditions:\t {scoreboard['conditions']}\n"
    
    if end_game:
        exit_string += f"{scoreboard['home_club'].name.upper()} ({scoreboard['home_club'].short_country}) {scoreboard['home_goal']} x {scoreboard['away_goal']} {scoreboard['away_club'].name.upper()} ({scoreboard['away_club'].short_country})\n"
        
        ''' Stats '''
        if verbose:
            exit_string += f"{stats['home_stats']['shots']} SHOTS {stats['away_stats']['shots']}\n"
            exit_string += f"{stats['home_stats']['shots on target']} SHOTS ON TARGET {stats['away_stats']['shots on target']}\n"
            exit_string += f"{stats['home_stats']['fouls']} FOULS {stats['away_stats']['fouls']}\n"
            exit_string += f"{stats['home_stats']['tackles']} TACKLES {stats['away_stats']['tackles']}\n"
            exit_string += f"{stats['home_stats']['saves']} SAVES {stats['away_stats']['saves']}\n"
            exit_string += f"{stats['home_stats']['ball possession']} BALL POSSESSION {stats['away_stats']['ball possession']}\n"
            exit_string += f"{stats['home_stats']['offsides']} OFFSIDES {stats['away_stats']['offsides']}\n"
            exit_string += f"{stats['home_stats']['free kicks']} FREE KICKS {stats['away_stats']['free kicks']}\n"
    
    else:
        exit_string += f"{scoreboard['home_club'].name.upper()} ({scoreboard['home_club'].short_country}) x {scoreboard['away_club'].name.upper()} ({scoreboard['away_club'].short_country})\n"
        return exit_string
    

    if end_game:
        ''' player_goal_string will return something like these
                (FLU) Player(Fred) 60'
        '''
        
        for tpl in scoreboard['home_player_goals'].items(): 
            goal_time = "" 
            for _ in range(tpl[-1]):
                goal_time += f"{randint(1,90)}' "
            player_goal_string += f"({home_club[0:3].upper()}) {tpl[0].name} {goal_time}\n"

        for tpl in scoreboard['away_player_goals'].items():
            goal_time = ""
            for _ in range(tpl[-1]):
                goal_time += f"{randint(1,90)}' " 
            player_goal_string += f"({away_club[0:3].upper()}) {tpl[0].name} {goal_time}\n" 

        return exit_string, player_goal_string # show the players scoreboard
