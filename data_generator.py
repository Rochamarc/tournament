from db.players_controller import PlayersController
from db.skills_controller import SkillsController

from random import randint

players_controller = PlayersController()
skills_controller = SkillsController()

def get_skill_by_position(position: str, club_class: str) -> list[int]:
    '''Define a list of values based on player position 
    
    Parameters
    ----------
    position : str
        Argument that defines how his skills are gonna be calculated
    club_class : str
        A 1 length string value that referes to A, B, C or D

    Returns
    -------
        A list of integer values
    '''
    
    if position == 'GK' : return [ get_skill_by_class(club_class) for _ in range(3) ]

    if position in ['CB','LB','RB','DM']:
        return [ get_skill_by_class(club_class) for _ in range(3) ] + [ get_skill_by_class(club_class) for _ in range(3)]
    return [ get_skill_by_class(club_class) for _ in range(3) ] + [ get_skill_by_class(club_class) for _ in range(3) ]

def get_skill_by_class(club_class: str) -> int:
    """Generate data based on value on club clubs

    Parameters
    ----------
    club_class : str
        A 1 length string value that referes to A, B, C or D
    
    Returns 
    -------
        A random int value
    """

    # Table of values based on club class
    # A -> 80 - 90
    # B -> 70 - 80
    # C -> 60 - 70
    # D -> 50 - 60

    # very shitty code
    if club_class == 'A':
        return randint(80,90)
    elif club_class == 'B':
        return randint(70,80)
    elif club_class == 'C':
        return randint(60,70)
    else:
        return randint(50,60)
        

def generate_players_skills(season: str, players: list, club_class: str) -> None:
    """Generate skill data for players

    Parameters
    ----------
    season : str
        A string with season value for the skill
    players : list
        A list containing player's data with: id and position
    club_class : str
        A 1 length string between A and D
    

    Returns
    -------
        A list of lists containing skills data 
    """ 
    
    player_skills = []

    for player in players:
        player_id = player[0]
        player_position = player[-1]

        data = get_skill_by_position(player_position, club_class)
        data.append(player_id)

        player_skills.append(data)
        
    return player_skills
    

if __name__ == "__main__":
    generate_players_skills('2022')