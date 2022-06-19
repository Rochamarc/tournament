from classes_helper import GenerateClass
from season import Season


# Class variables
gene = GenerateClass() 


# Global variables
season = input("Type the initial season: ")


for i in range(2):
    
    if season != '2021':
        gene.promotions_and_relegations(season) # initiate a new season

    ### SERIE A ###

    competition_name = "Campeonato Brasileiro Série A"
    division = 'serie_a'

    serie_a = Season(competition_name, season, division)
    serie_a.run()

    ### SERIE B ###

    competition_name = "Campeonato Brasileiro Série B"
    division = 'serie_b'

    serie_b = Season(competition_name, season, division)
    serie_b.run()

    ### END SERIE B ###


    ### SERIE C ###

    competition_name = "Campeonato Brasileiro Série C"
    division = 'serie_c'

    serie_c = Season(competition_name, season, division)
    serie_c.run()
    
    ### END SERIE C ###
    
    season = str(int(season) + 1) # next season
