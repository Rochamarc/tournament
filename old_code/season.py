from db.competition_controller import CompetitionData
from db.player_controller import PlayerData
from league import League
from outside_functions import open_file
from ranking import Ranking
from table import Table
from data_functions import prepare_player_to_retiring

import os
import sys 

flags = sys.argv

# Class variables 
table = Table()
ranking = Ranking()
competition = CompetitionData()
player_data = PlayerData()

if '-r' in flags : os.system('python init_db.py')

if '-h' in flags : open_file('help')

if '-i' in flags : os.system('python setting_international_clubs.py')

if '-d' in flags:
    season = '2021'
    n_seasons = 1
else:
    # Global variables
    season = input("Type the initial season: ")
    n_seasons = int(input("Type the number of seasons you wanna run: "))

for i in range(n_seasons):
    
    if season != '2021':
        table.promotions_and_relegations(season) # initiate a new season

    ### SERIE A ###

    competition_name = "Campeonato Brasileiro Série A"
    division = 'serie_a'

    serie_a = League(competition_name, season, division)
    serie_a.run()

    competition.insert_champion_db(competition_name, ranking.get_domestic_champion(division, season)[0], season)
    
    ### SERIE B ###

    competition_name = "Campeonato Brasileiro Série B"
    division = 'serie_b'

    serie_b = League(competition_name, season, division)
    serie_b.run()

    competition.insert_champion_db(competition_name, ranking.get_domestic_champion(division, season)[0], season)
    
    ### END SERIE B ###


    ### SERIE C ###

    competition_name = "Campeonato Brasileiro Série C"
    division = 'serie_c'

    serie_c = League(competition_name, season, division)
    serie_c.run()
    
    competition.insert_champion_db(competition_name, ranking.get_domestic_champion(division, season)[0], season)
    
    ### END SERIE C ###
    
    # retiring players
    print("Get and Save retirees")
    retirees = player_data. get_retiring_players() # get
    retirees = prepare_player_to_retiring(retirees) # prepare
    player_data.insert_retired_db(retirees) # Save in database
        
    print("Removing Retiring Players")
    player_data.remove_retired_playeres()
    


    season = str(int(season) + 1) # next season
