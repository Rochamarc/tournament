from random import choice 
from time import sleep
from pprint import pprint 
from classes_helper import GenerateClass
import pandas as pd
from db.database import InternationalCup 
from game import Game 

g = GenerateClass()
inter = InternationalCup()

class GroupStage:
    @staticmethod
    def define_group_stage(clubs_sorted, qualifying_phase, season, verbose=False):
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
                        clubs_sorted.append(temp) 

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
            return GroupStage.define_group_stage(ex_club_sorted, ex_qualifyin, season)

        for group, clubs in groups.items():
            group_name = f"group_{group}"
            inter.create_international_cup(season, group_name, verbose=True)
            inter.international_group_table_basic( [club.name for club in clubs], season, group_name, verbose=True)

        return groups

    @staticmethod
    def group_stage(group, group_list, competition, verbose=False):
        ''' Simulates the whole group phase from a single group
            Return a dict return { 'group': <class 'str'>, 'first place': <class 'club()'> , 'second place': <class 'club()'> }
        '''
        club_one, club_two, club_three, club_four = group_list[0], group_list[1], group_list[2], group_list[3]
        
        confronts = []
        for home in group_list:
            confronts += [ [ home, away ] for away in group_list if home != away ] # define every confront

        competition = 'Conmebol Libertadores'

        # Generating the matches
        for i in range(1,7):
            # series_data = [club_one.get_stats(),club_two.get_stats(),club_three.get_stats(),club_four.get_stats()] # extrating data stats
            
            df = pd.DataFrame(series_data, index=None, columns=['Club','Pts','Victory','Draw','Defeat','GS','GC','GB']) # create the dataframe
            sorted_data_frame = df.sort_values(by=['Pts','GB'], axis=0, ascending=False)
            print("")
            print(sorted_data_frame) 
            print("")

            Game(confronts[0][0], confronts[0][-1], competition, i).start()
            Game(confronts[-1][0], confronts[-1][-1], competition, i).start()

            del confronts[0]
            del confronts[-1]

            if i == 6:
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
    
    @staticmethod
    def define_knock_out_stage(teams, phase):
        """ Receive a dict and a string return a dict"""

        output = {}

        if phase == 'Round of 16':
            for confront in range(len(teams['first'])):
                first = choice(teams['first'])
                teams['first'].remove(first) # remove
                second = choice(teams['second'])
                teams['second'].remove(second) # remove

                output[f'confrontation {confront}'] = [first, second]

            return output 

        for confront in range(len(teams['classified'])):
            first = choice(teams['classified'])
            teams['classified'].remove(first) # remove
            second = choice(teams['classified'])
            teams['classified'].remove(second) # remove

            output[f'confrontation {confront}'] = [first, second]

        return output 


