from classes.club import Club
from classes_helper import GenerateClass
from database import ClubData, PlayerData

club_data = ClubData()
player_data = PlayerData()
generate = GenerateClass()

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

with open('files/latin_american_clubs/argentina.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['arg'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/bolivia.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['bol'].append(Club(name, country,cl_class))
        
with open('files/latin_american_clubs/chile.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['chi'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/colombia.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['col'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/ecuador.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['equ'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/paraguay.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['par'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/peru.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['per'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/uruguay.txt', encoding='UTF-8') as file:
    for i in file.readlines():
        i = i.split(',')
        name = i[0]
        country = i[1]
        cl_class = i[-1].replace('\n', '')
        clubs['uru'].append(Club(name, country,cl_class))

with open('files/latin_american_clubs/venezuela.txt', encoding='UTF-8') as file:
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
        players = generate.set_players(team, team.country, team.min_coeff, team.max_coeff)

        player_data.insert_players_db(players)