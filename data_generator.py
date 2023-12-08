from random import randint


def get_skill_by_position(position: str) -> list[int]:
    '''Define a list of values based on player position 
    
    Parameters
    ----------
    position : str
        Argument that defines how his skills are gonna be calculated

    Returns
    -------
        A list of integer values
    '''
    
    if position == 'GK' : return [ randint(55,99) for _ in range(3) ]

    if position in ['CB','LB','RB','DM']:
        return [ randint(55,99) for _ in range(3) ] + [ randint(35,85) for _ in range(3)]
    return [ randint(35,85) for _ in range(3) ] + [ randint(55,99) for _ in range(3) ]