from classes.club import Club
from helper import Helper
from db.club_controller import ClubData
from db.player_controller import PlayerData

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

with open('files/latin_american_clubs/argentina.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['arg'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/bolivia.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['bol'].append(Club(name, country,cl_class))
        
with open('files/latin_american_clubs/chile.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['chi'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/colombia.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['col'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/ecuador.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['equ'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/paraguay.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['par'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/peru.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['per'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/uruguay.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['uru'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/venezuela.csv', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['ven'].append(Club(name, country,cl_class))
        
# Saving clubs on database
for country, teams in clubs.items():
    club_data.insert_clubs_db(teams)

    for team in teams:
        players = helper.set_players(team, team.country, team.min_coeff, team.max_coeff)

        player_data.insert_players_db(players)
