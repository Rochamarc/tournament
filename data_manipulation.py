
def tuple_to_list(data: list) -> list[list]:
    """Change a list of sets or tuples to list objects """

    return [ list(a) for a in data ]

def change_to_a(data: list) -> list[list]:
    """Change the division id to 1 """

    for a in data:
        a[-1] = 1
    return data 

def change_to_b(data: list) -> list[list]:
    """Change the division id to 2 """

    for a in data:
        a[-1] = 2
    return data 

def change_to_c(data: list) -> list[list]:
    """Change the division id to 3 """

    for a in data:
        a[-1] = 3
    return data 

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
    

def relegate_serie_a(championships_data: list, next_season: str) -> dict:
    """Manipulate championships to to separate clubs that will stay in the
    serie a division to the relegated

    Parameters
    ----------
    championships_data : list
        A list of sets with [ club_id, division_id ]
    
    Returns
    -------
        A dict with { remains: [ [club_id, division_id, next_season] ], relegated: [ [club_id, serie_b_division_id, next_season] ] }
    """

    championships_data = tuple_to_list(championships_data)
    championships_data = [ [next_season] + i for i in championships_data ]

    return {
        'remains': championships_data[0:16],
        'relegated' : change_to_b(championships_data[16:20])
    }


def relegate_serie_b(championships_data: list, next_season: str) -> dict:
    """Manipulate championships to to separate clubs that will stay in the
    serie b division to the relegated

    Parameters
    ----------
    championships_data : list
        A list of sets with [ club_id, division_id ]
    
    Returns
    -------
        A dict with { remains: [ [club_id, division_id, next_season] ], relegated: [ [club_id, serie_b_division_id, next_season] ] }
    """

    championships_data = tuple_to_list(championships_data)
    championships_data = [ [next_season] + i for i in championships_data ]

    return {
        'promoted': change_to_a(championships_data[0:4]),
        'remains': championships_data[4:16],
        'relegated' : change_to_c(championships_data[16:20])
    }

def relegate_serie_c(championships_data: list, next_season: str) -> dict:
    """Manipulate championships to to separate clubs that will stay in the
    serie c division to the relegated

    Parameters
    ----------
    championships_data : list
        A list of sets with [ club_id, division_id ]
    
    Returns
    -------
        A dict with { remains: [ [club_id, division_id, next_season] ], relegated: [ [club_id, serie_b_division_id, next_season] ] }
    """

    championships_data = tuple_to_list(championships_data)
    championships_data = [ [next_season] + i for i in championships_data ]

    return {
        'promoted': change_to_b(championships_data[0:4]),
        'remains': championships_data[4:20]
    }


if __name__ == "__main__":
    print(relegate_serie_a([ i for i in range(1,21) ]))