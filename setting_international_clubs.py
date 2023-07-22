from classes.club import Club
from helper import Helper
from db.club_controller import ClubData
from db.player_controller import PlayerData

from outside_functions import filter_line_for_international_club

club_data = ClubData()
player_data = PlayerData()
helper = Helper()

clubs = {
    'arg': [],
    'bol': [],
    'chi': [],
    'col': [],
    'equ': [],
    'par': [],
    'per': [],
    'uru': [],
    'ven': []
}

# with the files openning we define the Club class instance

with open('files/latin_american_clubs/argentina.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['arg'].append(Club(club['name'], club['country'], club['cl_class']))

with open('files/latin_american_clubs/bolivia.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['bol'].append(Club(club['name'], club['country'], club['cl_class']))
        
with open('files/latin_american_clubs/chile.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['chi'].append(Club(club['name'], club['country'], club['cl_class']))

with open('files/latin_american_clubs/colombia.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['col'].append(Club(club['name'], club['country'], club['cl_class']))
    
with open('files/latin_american_clubs/ecuador.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['equ'].append(Club(club['name'], club['country'], club['cl_class']))
    
with open('files/latin_american_clubs/paraguay.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['par'].append(Club(club['name'], club['country'], club['cl_class']))

with open('files/latin_american_clubs/peru.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['per'].append(Club(club['name'], club['country'], club['cl_class']))
        
with open('files/latin_american_clubs/uruguay.csv', encoding='UTF-8') as file:
    for line in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['uru'].append(Club(club['name'], club['country'], club['cl_class']))

with open('files/latin_american_clubs/venezuela.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        club = filter_line_for_international_club(line)
        clubs['ven'].append(Club(club['name'], club['country'], club['cl_class']))
        
# Saving clubs on database
for country, teams in clubs.items():
    club_data.insert_clubs_db(teams) # he we save the international clubs

    for team in teams:
        # he we save the playes
        players = helper.set_players(team, team.country, team.min_coeff, team.max_coeff)
        player_data.insert_players_db(players)
