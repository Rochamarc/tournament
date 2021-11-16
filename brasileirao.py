from classes_helper import *
from classes import *
from game import Game 
from pprint import pprint 
from ranking import *
from database import *
import os 

os.system('./reset_database.sh') # reseting the database

gene = GenerateClass() 
rk = Ranking()
clubs = []
stadiums = []


competition_name = "Campeonato Brasileiro Série A"
season = "2021"

create_domestic_table(season) # Create the domestic table

schedule = {}

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
domestic_table_basic(club_names,season) # populate the database with basics

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

for clb in clubs:
    ''' Define a schedule '''
    schedule[clb] = [ club for club in clubs if club.name != clb.name ]


clubs_data = [ club.get_data() for club in clubs ] # this will return the data needed to create the table
tb = rk.table(clubs_data) # return a table
print(tb)

# Testing
ctn = input("Type enter to continue: ")

for home_club, home_matches in schedule.items():
    for away_club in home_matches:
        r_match = randint(1,38)
        # Start a new game
        g = Game(home_club, away_club, competition_name, r_match, head_stadium=choice(stadiums), verbose=False)
        result = g.start()
        update_domestic_table(result['home_team'], season) # home_team table update
        update_domestic_table(result['away_team'], season) # away_team table update

    clubs_data = [ club.get_data() for club in clubs ]
    tb = rk.table(clubs_data)
    print(tb)

players = gene.get_players_list(clubs) # this get the players list
'''
for player in players:
    print(player)
'''

insert_players_db(players) # insert into the database

