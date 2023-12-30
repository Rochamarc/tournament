def check_yes_no(other_values: list = []):
    """Asks for an input and check if the input is Y or n

    Parameters
    ----------
    other_values : list
        A default empty lists, add other valid values for input 

    Raises
    ------
        ValueError if the value passed on input is invalid

    Return
    ------
        A string containing a valid value for 'yes' or 'no'
    """

    value = input("Do you wanna procede [Y/n]: ")

    if value not in ['Y', 'n'] + other_values:
        raise ValueError(f'{value} is not valid! Try again!')
        
    return value


def check_for_season():
    """Asks for an input and check if the input is a string value that can be 
    convert as an integer and if the value has length of 4

    Raises
    ------
        ValueError if the len is diff than 4
        TypeError if the value cannot be convert to an integer

    Returns
    -------
        A string containing a valid value for season
    """

    value = input("Type the season: ")

    if len(value) != 4:
        raise ValueError(f'{value} is not valid! Type a value with 4 length') 

    try:
        int(value)
    except:
        raise TypeError(f'{value} is not valid to be a season! Type an int value')
    
    return value