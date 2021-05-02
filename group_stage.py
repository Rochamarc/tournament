from game_match import Game
import pandas as pd 
from time import sleep 
from ranking import update_player_stats

def group_stage(group, group_list, competition, verbose=False):
    """ Retorna um dicionario """
    club_one, club_two, club_three, club_four = group_list[0], group_list[1], group_list[2], group_list[3]

    # Gerando as seis partidas
    for i in range(1,7):
        # Definindo e mostrando a tabela
        series_data = [club_one.get_stats(),club_two.get_stats(),club_three.get_stats(),club_four.get_stats()]
        # Cria a tabela
        df = pd.DataFrame(series_data, index=None, columns=['Club','Pts','Victory','Draw','Defeat','GS','GC','GB'])
        sorted_data_frame = df.sort_values(by=['Pts','GB'], axis=0, ascending=False)
        print("")
        print(sorted_data_frame)
        print("")

        print(f"Group: {group}\nRound {i} of 6")
        
        # Rodada 1 de 6
        if i == 1:
            # club_one x club_two
            Game.game_match(i, competition, club_one,club_two)
            # club_three x club_four
            Game.game_match(i, competition, club_three,club_four)
            if verbose:
                sleep(2)
        elif i == 2:
            # club_one x club_four
            Game.game_match(i, competition, club_one,club_four)
            # club_two x club_three
            Game.game_match(i, competition, club_two,club_three)
            if verbose:
                sleep(2)
        elif i == 3:
            # dotmund x club_one
            Game.game_match(i, competition, club_three,club_one)
            # club_four x club_two
            Game.game_match(i, competition, club_four,club_two)
            if verbose:
                sleep(2)
        elif i == 4:
            # club_two x club_one
            Game.game_match(i, competition, club_two,club_one)
            # club_four x club_three
            Game.game_match(i, competition, club_four,club_three)
            if verbose:
                sleep(2)
        elif i == 5:
            # club_four x club_one
            Game.game_match(i, competition, club_four,club_one)
            # dormtund x club_two 
            Game.game_match(i, competition, club_three,club_two)
            if verbose:
                sleep(2)
        elif i == 6:
            # club_one x club_three
            Game.game_match(i, competition, club_one,club_three)
            # club_two x club_four
            Game.game_match(i, competition, club_two,club_four)
            if verbose:
                sleep(2)

            # Salvando os stats da ultima rodada!
            series_data = [club_one.get_stats(),club_two.get_stats(),club_three.get_stats(),club_four.get_stats()]
            df = pd.DataFrame(series_data, index=None, columns=['Club','Pts','Victory','Draw','Defeat','GS','GC','GB'])
            sorted_data_frame = df.sort_values(by=['Pts','GB'], axis=0, ascending=False)
        else:
            print("END GROUP STAGE")
        
    print(sorted_data_frame)
    if verbose:
        cont = input("Continue...")
    
    f_name = sorted_data_frame.iat[0,0]  
    s_name = sorted_data_frame.iat[1,0] 

    first = None
    second = None 

    for club in group_list:
        if club.name == f_name:
            first = club
        if club.name == s_name:
            second = club 

    update_player_stats(group_list) # update average

    return { 'group': group, 'first place': first, 'second place': second }
