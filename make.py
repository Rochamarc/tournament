import random  

def generate_player_hash(player_overall: int, weight: int=9, power: float=1.3) -> set[float]:
    """Generate a list of unique float values between zero and one

    Parameters
    ----------
    player_overall : int
        A value between 0 and 100
    
    Return
    ------
    list : float
        A list with random float values
    """
    rng_value = int(player_overall * weight**power)

    return set([round(random.random(), 4) for _ in range(rng_value) ])
    
if __name__ == "__main__":
    values = generate_player_hash(86)

    for _ in range(10):
        val = round(random.random(), 4)
        print(val in values)

# Tabela, amostra de acertos 
# 10e2 => 100 -> 0 acertos
# 10e3 => 1000 -> 1 acerto
# 10e4 => 10000 -> 7 acertos