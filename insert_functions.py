def check_yes_no(other_values: list = []):
    """Will ask for user to type an Y or n

    Return
    ------
        One digit string with Y or n
    """

    value = input("Do you wanna procede [Y/n]: ")

    if value not in ['Y', 'n'] + other_values:
        raise ValueError(f'{value} is not valid! Try again!')
        exit()
        
    return value


def check_for_season():
    """Check if the user type a viable value for season

    Returns
    -------
        A string containing a season
    """

    value = input("Type the season: ")

    if len(value) != 4:
        raise ValueError(f'{value} is not valid! Type a value with 4 length') 

    try:
        int(value)
    except:
        raise TypeError(f'{value} is not valid to be a season! Type an int value')
    
    return value