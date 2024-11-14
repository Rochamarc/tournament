from data_generator import apply_reduction

import numpy as np 
import random 

def simple_decision(p_overall) -> bool:
    """Calculates a decision based on players overall

    Parameters
    ----------
    p_overall : int
        An integer with players overall

    Returns
    -------
        A bool
    """
    
    return np.random.randint(1,30) < apply_reduction(p_overall, 0.25)

def complex_decision(p_overall: int, num_trials: int = 1) -> bool:
    """Calculates a decision based on players overall

    Parameters
    ----------
    p_overall : int
        An integer with players overall

    Returns
    -------
        A bool
    """

    p_overall = apply_reduction(p_overall, 0.25)
            
    # Garante que p_overall está no intervalo [0, 100]
    # p_overall = max(0, min(100, p_overall))

    # Calcula a probabilidade de sucesso
    p_success = 1 - p_overall / 50.0

    # Gera um número binomial com a probabilidade de sucesso
    result = np.random.binomial(num_trials, p_success)

    # Retorna True se o número de sucessos for 0 (mais frequentemente)
    return result == 0

def generate_player_hash(player_overall: int, weight: int=9, power: float=1.7) -> set[float]:
    """Generate a list of unique float values between zero and one

    Parameters
    ----------
    player_overall : int
        A value between 50 and 100
    weight : int
        A int value for the number that will be multiplied by the onverall
    power : float
        A float value for the power of the weight
        
    Return
    ------
    list : float
        A list with random float values
    """

    rng_value = int(player_overall * weight**power)

    return set([round(random.random(), 4) for _ in range(rng_value) ])

def complex_decision_2(player_hash: set) -> bool:
    """Generate a decision based on the player's hash

    Parameters
    ----------
    player_hash : set
        A set of automated values

    Returns
    -------
    bool : for the sorted value in player_hash
    """

    decision_value = round(random.random(), 4)

    return decision_value in player_hash