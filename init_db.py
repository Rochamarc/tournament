from classes.club import Club
from classes.stadium import Stadium
from helper import Helper

from db.club_controller import ClubData
from db.domestic_league_controller import DomesticLeague 
from db.player_controller import PlayerData
from db.stadium_controller import StadiumData

from outside_functions import filter_line_for_club, filter_line_for_stadium

from ranking import Ranking

import os 

from alive_progress import alive_bar

os.system('./db/reset_database.sh')

# Domestic cup
league = DomesticLeague()
ranking = Ranking()
std_data = StadiumData()
helper = Helper()
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
league.create_domestic_table('serie_a', '2021')
league.create_domestic_table('serie_b', '2021')
league.create_domestic_table('serie_c', '2021')

# Setting Generic Stadiums
with open('files/generic_stadiums/stadiums.csv', encoding='utf8') as file:
    for line in file.readlines():
        data = filter_line_for_stadium(line)
        generic_stadiums.append(Stadium(data['name'], data['location'])) 

# Setting Real Stadiums
with open('files/clubs_stadiums/stadiums.csv', encoding='utf8') as file:
    for i in file.readlines():
        data = filter_line_for_stadium(line, has_club_owner=True)
        stadiums.append(Stadium(data['name'], data['location'], capacity=data['capacity'], club_owner=data['club_owner']))

# Insert stadium data into database
print("Insert Stadium in database")
with alive_bar(2) as bar:
    std_data.insert_stadiums_db(stadiums)
    bar()
    std_data.insert_stadiums_db(generic_stadiums)
    bar()
    
# Serie A
with open('files/brasileirao/serie a/2021.csv', encoding='utf8') as file:
    ''' Creating clubs based on the files on the path above '''
    for line in file.readlines():
        data = filter_line_for_club(line) 
        country = 'BRA'
        serie_a.append(Club(data['name'], country, data['club_class'], state=data['state']))
    
# Serie B
with open('files/brasileirao/serie b/2021.csv', encoding='utf8') as file:
    ''' Creating clubs based on the files on the path above '''
    for line in file.readlines():
        data = filter_line_for_club(line) 
        country = 'BRA'
        serie_b.append(Club(data['name'], country, data['club_class'], state=data['state']))

# Serie C
with open('files/brasileirao/serie c/2021.csv', encoding='utf8') as file:
    ''' Creating clubs based on the files on the path above '''
    for i in file.readlines():
        data = filter_line_for_club(line) 
        country = 'BRA'
        serie_c.append(Club(data['name'], country, data['club_class'], state=data['state']))

# Insert clubs on the database
print("Inserting clubs on database")
with alive_bar(3) as bar:
    club_data.insert_clubs_db(serie_a)
    bar()
    club_data.insert_clubs_db(serie_b)
    bar()
    club_data.insert_clubs_db(serie_c)
    bar()

# Creating basic table
league.domestic_table_basic([ club.name for club in serie_a ], 'serie_a', '2021')
league.domestic_table_basic([ club.name for club in serie_b ], 'serie_b', '2021')
league.domestic_table_basic([ club.name for club in serie_c ], 'serie_c', '2021')

# Getting domestic table
tb_serie_a = ranking.domestic_table('serie_a', '2021')
tb_serie_b = ranking.domestic_table('serie_b', '2021')
tb_serie_c = ranking.domestic_table('serie_c', '2021')


print("Insert Players in database")
with alive_bar(60) as bar:
    for club in serie_a:
        ''' Generate player and formation '''
        players = helper.set_players(club, club.country, club.min_coeff, club.max_coeff)
        p_data.insert_players_db(players)
        bar()        

    for club in serie_b:
        ''' Generate player and formation '''
        players = helper.set_players(club, club.country, club.min_coeff, club.max_coeff)
        p_data.insert_players_db(players)
        bar()

    for club in serie_c:
        ''' Generate player and formation '''
        players = helper.set_players(club, club.country, club.min_coeff, club.max_coeff)    
        p_data.insert_players_db(players)
        bar()