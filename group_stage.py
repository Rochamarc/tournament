from game import Game
import pandas as pd 
from time import sleep 
from ranking import *
from classes import *
from classes_helper import GenerateClass

maraca = Stadium('Maracana', 'Rio de Janeiro, Brasil') # stadium test
g = GenerateClass()

def group_stage(group, group_list, competition, verbose=False):
    ''' Simulates the whole group phase from a single group
        Return a dict return { 'group': <class 'str'>, 'first place': <class 'club()'> , 'second place': <class 'club()'> }
    '''
    club_one, club_two, club_three, club_four = group_list[0], group_list[1], group_list[2], group_list[3]
    
    confronts = []
    for home in group_list:
        confronts += [ [ home, away ] for away in group_list if home != away ] # define every confront

    competition = 'Conmebol Libertadores'

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

        # print(f"Group: {group}\nRound {i} of 6")

        Game(confronts[0][0], confronts[0][-1], competition, i, maraca).start()
        Game(confronts[-1][0], confronts[-1][-1], competition, i, maraca).start()

        del confronts[0]
        del confronts[-1]

        if i == 6:
            # Salvando os stats da ultima rodada!
            series_data = [club_one.get_stats(),club_two.get_stats(),club_three.get_stats(),club_four.get_stats()]
            df = pd.DataFrame(series_data, index=None, columns=['Club','Pts','Victory','Draw','Defeat','GS','GC','GB'])
            sorted_data_frame = df.sort_values(by=['Pts','GB'], axis=0, ascending=False)
        
    
    print("END GROUP STAGE")
        
    print(sorted_data_frame)
    
    f_name = sorted_data_frame.iat[0,0]  
    s_name = sorted_data_frame.iat[1,0] 

    first = None
    second = None 

    for club in group_list:
        if club.name == f_name:
            first = club
        if club.name == s_name:
            second = club 

    g.update_player_stats(group_list) # update players average

    return { 'group': group, 'first place': first, 'second place': second }
