from game_match import match_actions
from random import randint 

"""
Competicao:
Rodada:
Jogo: 
Ida: (em caso de jogo 2)
Placar: 
Gol Qualificado: (em caso de gol qualificado)
Pealtis: (em caso de penaltis)
"""

def knock_out_match(game_stats, verbose=False):
    """ Receive a dict and return the same dict updated"""

    home_team = game_stats['home_team']
    away_team = game_stats['away_team']

    penalty = False 
    qualified_goal = False 

    if verbose:
        print(f"""
Competição: {game_stats['competition']}
Rodada: {game_stats['round']}
Jogo: {game_stats['game']} de {1 if game_stats['round'] == 'Final' else 2 }
{home_team.name.upper()} ({home_team.short_country}) 0 x 0 {away_team.name.upper()} ({away_team.short_country})
    """)

    out_string = f"""
Competição: {game_stats['competition']}
Rodada: {game_stats['round']}
Jogo: {game_stats['game']} de {1 if game_stats['round'] == 'Final' else 2}
"""

    home_goals = 0 # variaveis comecando 0
    away_goals = 0 # variaveis comecando 0

    total_home = game_stats['home_goal'] # variaveis somando os gols da partida anterior
    total_away = game_stats['away_goal'] # variaveis somando os gols da partida anterior

    goals = match_actions(home_team, away_team, 45) # Normal Time Actions
    home_goals += goals['home_goal']
    away_goals += goals['away_goal']

    total_home += home_goals # partida anterior + partida atual -> fim de tempo normal
    total_away += away_goals # partida anterior + partida atual -> fim de tempo normal


    e_home_goals = 0
    e_away_goals = 0

    # EXTRA TIME
    # only in the final match 
    if game_stats['round'] == 'Final':

        e_goals = match_actions(home_team, away_team, 15)
        e_home_goals += e_goals['home_goal']
        e_away_goals += e_goals['away_goal']
        
    # QUALIFIED GOAL
    # from round_16 to semi_finals
    if total_home == total_away and game_stats['game'] == 2:
        """ Verifica o gol qualificado """
        f_home_goals = game_stats['home_goal']
        f_away_goals = game_stats['away_goal']

        if f_home_goals > away_goals:
            qualified_goal = True 
            game_stats['winner'] = home_team
            game_stats['loser'] = away_team
            q_score = f"\u0332{f_home_goals} - {f_away_goals}"

        elif away_goals > f_home_goals:
            qualified_goal = True
            add_points(away_team) 
            game_stats['loser'] = home_team
            game_stats['winner'] = away_team 
            q_score = f"{home_goals} - \u0332{away_goals}"

    
    total_home += e_home_goals # Somos todos os gols com os da prorrogação 
    total_away += e_away_goals # Somos todos os gols com os da prorrogação 
    
    # Verifica se a partida vai pros penaltis
    if total_home == total_away:
        if not qualified_goal:
            if game_stats['game'] == 2 or game_stats['round'] == 'Final':
                penalty = True 

    # PENALTY
    # works fine, all the knock_out matches have penaltys
    if penalty: 
        p_home = 0  
        p_away = 0

        for i in range(10):
            if i % 2 == 0:
                # penalty away
                shot = randint(1,6)
                defense = randint(1,5)
                if shot != defense:
                    if shot != 6: 
                        p_home += 1
            else:
                # penalty away
                shot = randint(1,6)
                defense = randint(1,5)
                if shot != defense:
                    if shot != 6:
                        p_away += 1

        # Sudden death
        if p_home == p_away:
            while p_home == p_away:

                shot_1 = randint(1,6)
                defense_1 = randint(1,5)
                
                if shot_1 != defense_1:
                    if shot_1 != 6:
                        p_home += 1
                
                shot_2 = randint(1,6)
                defense_2 = randint(1,5)

                if shot_2 != defense_2:
                    if shot_2 != 6:
                        p_away += 1

        # Salvo as estatisticas no dicionario de saida
        game_stats['penalty_home'] = p_home 
        game_stats['penalty_away'] = p_away
    
    home_goals += e_home_goals
    away_goals += e_away_goals

    if game_stats['game'] == 2:
        out_string += f"Ida: {game_stats['home_goal']} - {game_stats['away_goal']}\n"
    
    out_string += f"{home_team.name.upper()} ({home_team.short_country}) {home_goals} x {away_goals} {away_team.name.upper()} ({away_team.short_country})\n"
    
    if qualified_goal:
        out_string += f"GQ: {q_score}\n"

    if penalty:
        out_string += f"Pênaltis: {p_home} - {p_away}\n"

    print(out_string) 

    # WINNER REGISTRATION
    if total_home == total_away:
        if not qualified_goal:
            if game_stats['game'] == 2 or game_stats['round'] == 'Final':
                if p_home > p_away:
                    add_points(home_team)
                    game_stats['winner'] = home_team
                    game_stats['loser'] = away_team 
                else:
                    add_points(away_team)
                    game_stats['winner'] = away_team
                    game_stats['loser'] = home_team  
    if total_home > total_away:
        add_points(home_team)
        game_stats['winner'] = home_team 
        game_stats['loser'] = away_team
    if total_home < total_away:
        add_points(away_team)
        game_stats['winner'] = away_team
        game_stats['loser'] = home_team  

    game_stats['home_goal'] += home_goals
    game_stats['away_goal'] += away_goals

    home_team.register_knock_out_game(home_goals, away_goals) 
    away_team.register_knock_out_game(away_goals, home_goals)    
    
    return game_stats

def add_points(winner_team):
    for player in winner_team.start_eleven:
        player.points += 1