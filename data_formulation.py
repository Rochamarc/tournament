# Print data readble 

def pretty_print(data: list) -> None:
    """Print database data for humans

    Parameters
    ----------
    data : list
        A list of sets of data 
    
    Returns
    -------
        None
    """

    for item in data:
        print(*item)

def print_stars(string_value: str) -> None:
    """Print a string_value between dashes and line breaker

    Parameters
    ----------
    string_value : str
        A printable string value

    Returns
    -------
        None
    """
    
    l = len(string_value)

    print('-' * l)
    print('\n')
    print(string_value)
    print('\n')
    print('-' * l)