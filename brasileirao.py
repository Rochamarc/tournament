from classes_helper import *
from classes import *
from game import Game  
from ranking import *
from database import *
import os 

os.system('./reset_database.sh') # reseting the database

gene = GenerateClass() 
rk = Ranking()
clubs = []
stadiums = []
matches = []

competition_name = "Campeonato Brasileiro Série A"
season = "2021"

create_domestic_table(season) # Create the domestic table

#
#
#
# Setting and config
#
#
#

with open('files/brasileirao/serie a/2021.txt') as file:
    ''' Creating clubs based on the files on the path above '''
    for i in file.readlines():
        i = i.split(',') # split the string with two new strings
        name = i[0] # get thje club name
        state = i[-1].replace('\n', '') # get the club state
        country = 'Brasil'
        clubs.append(Club(name, country, state=state, skip_conf=True))

club_names = [ club.name for club in clubs ]
domestic_table_basic(club_names,season) #Insert intial domestic cup table to the db 

for club in clubs:
    players = gene.set_players(club.name, club.country, club.coeff) # dict of players
    club.set_formation(players) # sort and att the players to the club

with open('files/generic_stadiums/stadiums.txt') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        city = i[1]
        country = i[-1].replace('\n', '')
        location = f"{city}, {country}"
        
        # creating the stadiums
        stadiums.append(Stadium(name, location))

#
#
#
# Initializing
#
#
# 

schedule = gene.define_schedule(clubs,stadiums) # the schedule

for rnd, game_info in schedule.items():
    for match in game_info:
        matches.append(Game(match[0], match[1], competition_name, int(rnd.split(' ')[-1]), head_stadium=match[-1]))


tb = rk.table(season) # Get the initial domestic cup table
print(tb) # show the table

for match in matches:
    ''' execute the matches '''
    r = match.start()
    update_domestic_table(r['home_team'], season)
    update_domestic_table(r['away_team'], season)

    
tb = rk.table(season)
print(tb)
ctn = input("Type enter to continue: ")
    
for club in clubs:
    print(club.get_data())  

players = gene.get_players_list(clubs) # this get the players list

insert_players_db(players) # insert into the database