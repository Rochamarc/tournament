from database import ClubData, PlayerData, StadiumData
from ranking import Ranking

import os

stadium_data = StadiumData()
p_data = PlayerData()
c_data = ClubData()
rk = Ranking()  

help_string = '''
get_players -> [club_name]  -> Get a list o players
get_table -> [division] [season] -> Get the division table
'''


history = 0
while True:
    history += 1

    action = input(f"SoccerGameApi_[{history}]_$ ")


    if action == 'exit' : exit() # exit

    if action == 'help': print(help_string)

    if action == 'clear' : os.system('clear')

    if 'get_players' in action:
        ''' Getting players '''
        club_name = action.split(' ')[-1]

        players = p_data.get_players(club_name)

        print(rk.player_info(players))

    if 'get_table' in action:
        ''' Get domestic league table '''
        division = action.split(' ')[1]
        season = action.split(' ')[-1]

        tb = rk.domestic_table(division, season)
        print(tb)

    if 'get_stadiums' in action:
        ''' Get stadiums '''

        stadiums = stadium_data.get_stadiums()

        for stadium in stadiums:
            print(stadium)

    if 'set_clubs' in action:
        ''' Get info from a club '''
