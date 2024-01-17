def tuple_to_list(data: list) -> list[list]:
    """Convert a list of sets or tuples to list objects

    Parameters
    ----------
    data : list
        A set of data
    
    Returns
    -------
        A python list objects of the inserted data
    """

    return [ list(a) for a in data ]

def change_to_a(data: list) -> list[list]:
    """Change the division id to 1

    Parameters
    ----------
    data : list
        A list of lists with club's information

    Returns
    -------
        The data list with updated id value 
    """

    for a in data:
        a[-1] = 1
    return data 

def change_to_b(data: list) -> list[list]:
    """Change the division id to 2

    Parameters
    ----------
    data : list
        A list of lists with club's information

    Returns
    -------
        The data list with updated id value 
    """

    for a in data:
        a[-1] = 2
    return data 

def change_to_c(data: list) -> list[list]:
    """Change the division id to 3

    Parameters
    ----------
    data : list
        A list of lists with club's information

    Returns
    -------
        The data list with updated id value 
    """

    for a in data:
        a[-1] = 3
    return data 

def fomrmulate_clubs_to_simple_cup(data_1: list, data_2: list) -> list:
    """Formulate club's id for sort confronts

    Paramters
    ---------
    data_1 : list
        A list of lists, sets or tuples with club_id data
    data_2 : list
        A list of lists, sets or tuples with club_id data
    
    Returns
    -------
        A one dimentional list combined by the two data lists
    
    Raises
    ------
    Exception
        If the final data length is odd
    """
    
    data_1 = [ d[0] for d in data_1 ]
    data_2 = [ d[0] for d in data_2 ]

    data = data_1 + data_2
    
    l_data = len(data)

    if not l_data % 2 == 0:
        raise Exception("The sum of length of data_1 + data_2 = {} is odd, this has to be even".format(l_data))
    return data_1 + data_2
    

def formulate_clubs_to_championships(data_1: list, data_2: list, data_3: list) -> list:
    """Change promoted, relegated and remains clubs to next season

    Parameters
    ----------
    data_1 : list
        A list of data of clubs that remains in the division
    data_2 : list
        A list of data (promoted or relegated) that change divison
    data_3 : list
        A list of data (promoted or relegated) that change divison. ps:Use an empy list if this data will not be usefull
    
    Returns
    -------
        A list of of data with len = numbers of clubs per division
    """

    return data_1 + data_2 + data_3
    

def relegate_brazillian_tournament(championships_data: list, next_season: str, division: str) -> dict:
    """Manipulate championships to to separate clubs that will stay in the
    serie a division to the relegated

    Parameters
    ----------
    championships_data : list
        A list of sets with [ club_id, division_id ]
    next_season : int
        Int value for the next season 
    division : str
        A value for division: serie_a, serie_b, or serie_c 
    
    Returns
    -------
        A dict with { remains: [ [club_id, division_id, next_season] ], relegated: [ [club_id, serie_b_division_id, next_season] ] }
    """

    championships_data = tuple_to_list(championships_data)
    # sum a list with [next_season] value with all [club_id, division_id ] for each club
    championships_data = [ [next_season] + club_data for club_data in championships_data ]

    # Get the clubs that stays in serie_a and the clubs that are being relegated
    
    if division == 'serie_a':
        result = {
            'remains': championships_data[0:16],
            'relegated' : change_to_b(championships_data[16:20])
        }
    elif division == 'serie_b':
        result = {
        'promoted': change_to_a(championships_data[0:4]),
        'remains': championships_data[4:16],
        'relegated' : change_to_c(championships_data[16:20])
        }
    else:
        result = {
        'promoted': change_to_b(championships_data[0:4]),
        'remains': championships_data[4:20]
        }

    return result


def formulate_data_for_market_value(players_data: list, players_overall: list) -> list[list]:
    """Formulate players_data and overall_data

    Parameters
    ----------
    players_data: list
        A list of players data
    skills_data : list
        A list of overall and id 
    
    Raises
    ------
        Exception if the len of the two datas are not the same size
        
    Returns
    -------
        A list of lists with player_id, birth, position & overall
    """

    if len(players_data) != len(players_overall):
        raise Exception(f'players_data length {len(players_data)} is different from players_overall length {len(players_overall)}')

    data = []

    for pos in range(len(players_data)):
        p_data = []

        p_data += players_data[pos]

        for over in players_overall:
            if p_data[0] == over[-1]:
                p_data.append(over[0]) 

        data.append(p_data)
    
    return data 

def prepare_player_stats_to_db(player_stats: dict, season: str, game_id: int) -> list[list]:
    """Prepare a list of data to insert into tournament.stats schema

    Parameters
    ----------
    player_stats : dict
        Stats from Game.logs['stats'] format
    season : str
        A str with season 
    game_id : int
        A integer of the id from the game

    Returns
    -------
        A list of list with tournament.stats data
    """
    player_data = []

    for _, item in player_stats.items():
        data = [
            season,
            item['matches'],
            item['shots'],
            item['shots_on_target'],
            item['goals'],
            item['assists'],
            item['fouls_committed'],
            item['tackles'],
            item['passes'],
            item['wrong_passes'],
            item['intercepted_passes'],
            item['clearances'],
            item['stolen_balls'],
            item['clean_sheets'],
            item['defenses'],
            item['difficult_defenses'],
            item['goals_conceded'],
            item['player_id'],
            game_id
        ]

        player_data.append(data)

    return player_data