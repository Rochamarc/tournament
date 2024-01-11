from random import randint

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
        

def generate_players_skills(players: list, club_class: str) -> list[list]:
    """Generate skill data for players

    Parameters
    ---------- 
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

def define_extension_by_age(age: int, season: str) -> str:
    """Generates a contract extension based on player's age

    Parameters
    ----------
    age : int
        A integer value for player's age
    season : str
        A string for initial season
    
    Returns
    -------
        A four digit int value for end season
    """

    four_to_six = age >= 16 and age <= 22
    three_to_five = age > 22 and age <= 27
    two_to_three = age > 27 and age <= 31
    one_to_two = age > 31

    if four_to_six:
        extension = randint(4,6)
    elif three_to_five:
        extension = randint(3,5)
    elif two_to_three:
        extension = randint(2,3)
    elif one_to_two:
        extension = randint(1,2)
    else:
        raise ValueError(f'{age}')

    return str(extension + int(season))

def generate_player_contracts(players: list, club_id: int, current_season: str) -> list[list]:
    """Generates contracts data between players and clubs

    Parameters
    ----------
    players : list
        A list of lists contining players data: id & birth
    club_id : int
        A integer value for club id
    current_season : str
        A string value with the current season. this will be the start value on contract

    Returns
    -------
        A list of lists containing player_contracts data
    """

    # TODO add transfer amount and termination fine as a none default varibles
    # insert these variable through the query, to do this change the query
    # to insert all columns from the player_contracts 

    player_contracts = []

    for player in players:
        player_id = player[0]

        # used to define extension
        age = int(current_season) - int(player[-1]) 

        start = current_season
        end = define_extension_by_age(age, current_season)
        salary = 100_000 

        contract_data = [ start, end, salary, club_id, player_id ]

        player_contracts.append(contract_data)
   
    return player_contracts

if __name__ == "__main__":
    pass