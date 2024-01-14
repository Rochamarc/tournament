from random import randint
from data_manipulation import apply_reduction

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
        A list of lists contining players data: id, birth & position
    club_id : int
        A integer value for club id
    current_season : str
        A string value with the current season. this will be the start value on contract

    Returns
    -------
        A list of lists containing player_contracts data
    """

    player_contracts = []

    for player in players:
        player_id = player[0]

        # used to define extension
        age = int(current_season) - int(player[1]) 

        # columns of player_contracts by order
        start = current_season
        end = define_extension_by_age(age, current_season)
        transfer_amount = None
        salary = 100_000 
        termination_fine = None 

        contract_data = [ start, end, transfer_amount, salary, termination_fine, club_id, player_id ]

        player_contracts.append(contract_data)
   
    return player_contracts

def calculate_overall_per_player(values: list) -> list[int]:
    """Calculate the overall of a player by list
    
    Parameters
    ----------
    values : list
        A list of lists with skills values and player_id 

    Returns
    -------
        A list of average mean of skills
    """
    
    res = []

    for value in values:
        value = list(value)
        player_id = value.pop()

        # remove the zeros 
        v = [ i for i in value if i != 0 ]

        # calculate average
        avg = sum(v) // len(v) if len(v) > 0 else 0

        res.append([avg, player_id])

    return res

def define_value_by_age(age: int, overall: int=0) -> int:
    """Calculate a partial value for market value based on player's age

    Parameters
    ----------
    age : int
        A valid integer value for a player age
    overall : int
        An integer value that matches his overall skills

    Returns
    -------
        An int value 5_000 and 100_000
    """
    # TODO for now, the overall it's not gonna be
    # used, add this calc before this scope is running fine

    # 16_22 -> min 10_000 max 50_000 
    # 23_28 -> min 40_000 max 100_000 
    # 29_32 -> min 20_000 max 40_000 
    # 33_ -> min 5_000 max 10_000 

    if age >= 33:
        return randint(5_000, 10_000)
    elif 29 <= age <= 32:
        return randint(20_000, 40_000)
    elif 23 <= age <= 28:
        return randint(40_000, 100_000)
    else:
        return randint(10_000, 50_000)

def define_value_by_position(position: str, overall: int=0) -> int:
    """Calculate a partial value for market value based on player's position

    Parameters
    ----------
    position : str
        A valid string value for a position
    overall : int
        An integer value that matches his overall skills

    Returns
    -------
        An int value between 5_000 and 100_000
    """

    # TODO for now, the overall it's not gonna be
    # used, add this calc before this scope is running fine

    # GK -> min 5_000  max 10_000 
    # DEF -> min 5_000 max 20_000
    # MID -> min 5_000 max 50_000
    # AT -> min 10_000 max 100_000 
    
    if position == 'GK':
        return randint(5_000, 10_000)
    
    if position in ['RB','LB', 'CB']:
        return randint(5_000, 20_000)
    elif position in ['DM','AM','LM','RM','CM']:
        return randint(5_000, 50_000)
    else:
        return randint(10_000, 100_000)

def define_value_by_overall(overall: int) -> int:
    """Calculate a partial value for the market value based on player's position

    Parameters
    ----------
    overall : int
        An integer that matches his overall skills

    Returns
    -------
        An int value between 1_000 and 90_000
    """
    
    red_overall = apply_reduction(overall, 0.1)
    
    # the red_overall goes from 5 to 10
    # so we have basically 5 categories of values
    #

    if red_overall == 5:
        return randint(1_000, 5_000)
    if red_overall == 6:
        return randint(10_000, 20_000)
    if red_overall == 7:
        return randint(20_000, 30_000)
    if red_overall == 8:
        return randint(50_000, 60_000)
    else:
        return randint(70_000, 90_000)


def calculate_market_value(players_data: list, season: str) -> list[list]:
    """Calculate the market value for the player

    Parameters
    ----------
    players_data : list
        A list containing players information as: id, birth, position, overall (for now thats all the data i need)
    season : str
        A string containing a valid value for season

    Returns
    -------
        A list of list containing the season, market_value & player's id (the market_value table columns)    
    """
    
    data = []

    for player in players_data:
        # get the id
        player_id = player[0]

        # get the player's age
        age = int(season) - int(player[1])
        position = player[2] 
        overall = player[-1]

        # first step of defining a partial value
        market_value = define_value_by_age(age)
        market_value += define_value_by_position(position)
        market_value += define_value_by_overall(overall)    

        data.append([ season, market_value, player_id ])

    return data

if __name__ == "__main__":
    pass