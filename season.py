from classes_helper import GenerateClass
from db.database import CompetitionData
from league import League
from table import Table
from ranking import Ranking

import os

# Class variables
gene = GenerateClass() 
table = Table()
ranking = Ranking()
competition = CompetitionData()

# Reset database
reset = input("Type y for reset database: ")
if reset == 'y':
    os.system('python init_db.py')

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
    
    season = str(int(season) + 1) # next season
