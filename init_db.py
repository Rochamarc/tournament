from classes.club import Club
from classes.stadium import Stadium
from classes_helper import GenerateClass
from database import ClubData, DomesticLeague, PlayerData, StadiumData
from ranking import Ranking

import os 

os.system('./reset_database.sh')

# Domestic cup
league = DomesticLeague()
ranking = Ranking()
std_data = StadiumData()
gene = GenerateClass()
p_data = PlayerData()
club_data = ClubData()



serie_a = []
serie_b = []
serie_c = []
generic_stadiums = []
stadiums = []

# set generic players
# gene.set_generic_const_player() ta dando erro, depois eu resolvo

# creating tables on my local database
league.create_domestic_table('serie_a', '2021', verbose=True)
league.create_domestic_table('serie_b', '2021', verbose=True)
league.create_domestic_table('serie_c', '2021', verbose=True)

# Setting Generic Stadiums
with open('files/generic_stadiums/stadiums.txt', encoding='utf8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        city = i[1]
        country = i[-1].replace('\n', '')
        location = f"{city}, {country}"
        
        # creating the stadiums
        generic_stadiums.append(Stadium(name, location))

# Setting Real Stadiums
with open('files/clubs_stadiums/stadiums.txt', encoding='utf8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        capacity = i[1]
        city = i[2]
        country = i[3]
        location = f'{city}, {country}'
        club_owner = i[-1].replace('\n', '')
        stadiums.append(Stadium(name, location, capacity=capacity, club_owner=club_owner))

# Insert stadium data into database
std_data.insert_stadiums_db(stadiums, verbose=True)
std_data.insert_stadiums_db(generic_stadiums, verbose=True)

# Serie A
with open('files/brasileirao/serie a/2021.txt', encoding='utf8') as file:
    ''' Creating clubs based on the files on the path above '''
    for i in file.readlines():
        i = i.split(',') 
        name = i[0] 
        state = i[1].replace('\n', '')
        cl_class = i[-1].replace('\n', '') 
        country = 'BRA'
        serie_a.append(Club(name, country, cl_class, state=state))

    
# Serie B
with open('files/brasileirao/serie b/2021.txt', encoding='utf8') as file:
    ''' Creating clubs based on the files on the path above '''
    for i in file.readlines():
        i = i.split(',') 
        name = i[0] 
        state = i[1].replace('\n', '') 
        cl_class = i[-1].replace('\n', '')
        country = 'BRA'
        serie_b.append(Club(name, country, cl_class, state=state))



# Serie C
with open('files/brasileirao/serie c/2021.txt', encoding='utf8') as file:
    ''' Creating clubs based on the files on the path above '''
    for i in file.readlines():
        i = i.split(',') 
        name = i[0] 
        state = i[1].replace('\n', '') 
        cl_class = i[-1].replace('\n', '')
        country = 'BRA'
        serie_c.append(Club(name, country, cl_class, state=state))


# Insert clubs on the database
club_data.insert_clubs_db(serie_a)
club_data.insert_clubs_db(serie_b)
club_data.insert_clubs_db(serie_c)



# Creating basic table
league.domestic_table_basic([ club.name for club in serie_a ], 'serie_a', '2021', verbose=True)
league.domestic_table_basic([ club.name for club in serie_b ], 'serie_b', '2021', verbose=True)
league.domestic_table_basic([ club.name for club in serie_c ], 'serie_c', '2021', verbose=True)

# Getting domestic table
tb_serie_a = ranking.domestic_table('serie_a', '2021')
tb_serie_b = ranking.domestic_table('serie_b', '2021')
tb_serie_c = ranking.domestic_table('serie_c', '2021')


for club in serie_a:
    ''' Generate player and formation '''
    players = gene.set_players(club, club.country, club.min_coeff, club.max_coeff)
    
    p_data.insert_players_db(players)
    # player_api.post_players(players) 

for club in serie_b:
    ''' Generate player and formation '''
    players = gene.set_players(club, club.country, club.min_coeff, club.max_coeff)
    
    p_data.insert_players_db(players)
    # player_api.post_players(players)

for club in serie_c:
    ''' Generate player and formation '''
    players = gene.set_players(club, club.country, club.min_coeff, club.max_coeff)
    
    p_data.insert_players_db(players)
    # player_api.post_players(players)