from random import choice 
from time import sleep
from pprint import pprint 

# 32 equipes 
# potes 4 grupos de 8
# 8 grupos do A ao H com uma equipe de cada pote
# A unica definição previa é que o atual campeao fica como cabeca do grupo A

def define_group_stage(clubs_sorted, qualifying_phase, verbose=False):
    """ Lista de clubes, lista de nomes dos qualificados na pré e um argumento verbose opicional """
    
    ex_club_sorted = clubs_sorted.copy()
    ex_qualifyin = qualifying_phase.copy()

    try:
        # sorteados pelo ranking
        clubs_sorted.sort(key=lambda club : club.ranking_points, reverse=True) 

        for club in clubs_sorted:
            temp = None 

            for quali in qualifying_phase:
                if quali == club.name:
                    temp = club 
                    clubs_sorted.remove(temp)
                    clubs_sorted.append(temp) # add no final da lista

        pots = {
            "1": clubs_sorted[0:8],
            "2": clubs_sorted[8:16],
            "3": clubs_sorted[16:24],
            "4": clubs_sorted[24:32]
        }

        pprint(pots)

        groups = {
            "A" : [],
            "B" : [],
            "C" : [],
            "D" : [],
            "E" : [],
            "F" : [],
            "G" : [],
            "H" : []
        }

        # sorting pot 1
        for club in pots["1"]:
            print("Sorteando o pote 1")
            group_choices = ["A","B","C","D","E", "F", "G", "H"]

            for group, group_clubs in groups.items():
                if len(group_clubs) == 1:
                    group_choices.remove(group)

            group_sorted = choice(group_choices)

            if verbose:
                print(f"{club} foi sorteado para o grupo {group_sorted}")
                sleep(2) 
            groups[group_sorted].append(club)

        if verbose:
            pprint(groups)
            sleep(2)

        # sorting pot 2
        for club in pots["2"]:
            print("Sorteando o pote 2")
            group_choices = ["A", "B", "C", "D", "E", "F", "G", "H"]


            for group, group_clubs in groups.items():
                if len(group_clubs) == 2:
                    group_choices.remove(group)
                else:
                    for group_club in group_clubs:
                        if group_club.country == club.country:
                            group_choices.remove(group)


            group_sorted = group_choices[0] #choice(group_choices)
            
            if verbose:
                print(f"{club} foi sorteado para o grupo {group_sorted}")
                sleep(2)

            groups[group_sorted].append(club)

        if verbose:
            pprint(groups)
            sleep(2)
        
        # sorting pot 3
        for i in range(len(pots["3"])):
            print("Sorteando o pote 3")
            group_choices = ["A", "B", "C", "D", "E", "F", "G", "H"]

            club = choice(pots["3"])
            pots["3"].remove(club)

            for group, group_clubs in groups.items():
                if len(group_clubs) == 3:
                    group_choices.remove(group)
                else:
                    for group_club in group_clubs:
                        if group_club.country == club.country:
                            group_choices.remove(group)
            

            group_sorted = group_choices[0] # choice(group_choices)

            if verbose:
                print(f"{club} foi sorteado para o grupo {group_sorted}")
                sleep(2)

            groups[group_sorted].append(club)        

        # sorting pot 4
        for club in pots["4"]:
            print("Sorteando o pote 4")
            group_choices = ["A", "B", "C", "D", "E", "F", "G", "H"]

            for group, group_clubs in groups.items():
                if len(group_clubs) == 4:
                    group_choices.remove(group)

            group_sorted = choice(group_choices)
            
            if verbose:
                print(f"{club} foi sorteado para o grupo {group_sorted}")
                sleep(2)

            groups[group_sorted].append(club)
    
    except:
        define_group_stage(ex_club_sorted, ex_qualifyin)

    return groups