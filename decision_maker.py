from data_generator import apply_reduction

import numpy as np 

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