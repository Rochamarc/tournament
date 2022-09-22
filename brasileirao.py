from classes_helper import GenerateClass
from competition import Competition
from table import Table

import os

# Class variables
gene = GenerateClass() 
table = Table()

# Reset database
reset = input("Type y for reset database: ")
if reset == 'y':
    os.system('python init_db.py')

# Global variables
season = input("Type the initial season: ")
api_bool = False

for i in range(2):
    
    if season != '2021':
        table.promotions_and_relegations(season) # initiate a new season

    ### SERIE A ###

    competition_name = "Campeonato Brasileiro Série A"
    division = 'serie_a'

    serie_a = Competition(competition_name, season, division)
    serie_a.run(api=api_bool)

    ### SERIE B ###

    competition_name = "Campeonato Brasileiro Série B"
    division = 'serie_b'

    serie_b = Competition(competition_name, season, division)
    serie_b.run(api=api_bool)

    ### END SERIE B ###


    ### SERIE C ###

    competition_name = "Campeonato Brasileiro Série C"
    division = 'serie_c'

    serie_c = Competition(competition_name, season, division)
    serie_c.run(api=api_bool)
    
    ### END SERIE C ###
    
    season = str(int(season) + 1) # next season
