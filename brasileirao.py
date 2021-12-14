from classes_helper import GenerateClass
from classes import *
from game import Game  
from ranking import *
from database import DomesticLeague, PlayerData

# Class variables
gene = GenerateClass() 
league = DomesticLeague()
rk = Ranking()
p_data = PlayerData()

# Global variables
stadiums = [ gene.reconstruct_stadiums() ]
season = '2021'

### SERIE A ###
serie_a_matches = []

competition_name = "Campeonato Brasileiro Série A"
division = 'serie_a'


serie_a_clubs = gene.reconstruct_clubs(division, season)

schedule = gene.define_schedule(serie_a_clubs, stadiums[0]) # the schedule

for club in serie_a_clubs:
    club.set_formation(p_data.get_players(club.name))

for rnd, game_info in schedule.items():
    ''' Defining the schedule '''
    for match in game_info:
        print(match[0].start_eleven)
        serie_a_matches.append(Game(match[0], match[1], competition_name, int(rnd.split(' ')[-1]), season, head_stadium=match[-1]))


tb = rk.domestic_table(division, season) # Get the initial domestic cup table
print(tb) 

for match in serie_a_matches:
    ''' execute the matches '''
    r = match.start()
    match.save_game_database()
    league.update_domestic_table(r['home_team'], division, season)
    league.update_domestic_table(r['away_team'], division, season)


print(league.get_domestic_cup_table(division, season))
### END SERIE A ###

### SERIE B ###
serie_b_matches = []

competition_name = "Campeonato Brasileiro Série B"
division = 'serie_b'


serie_b_clubs = gene.reconstruct_clubs(division, season)

schedule = gene.define_schedule(serie_b_clubs, stadiums[0]) # the schedule

for club in serie_b_clubs:
    club.set_formation(p_data.get_players(club.name))

for rnd, game_info in schedule.items():
    ''' Defining the schedule '''
    for match in game_info:
        print(match[0].start_eleven)
        serie_b_matches.append(Game(match[0], match[1], competition_name, int(rnd.split(' ')[-1]), season, head_stadium=match[-1]))


tb = rk.domestic_table(division, season) # Get the initial domestic cup table
print(tb) 

for match in serie_b_matches:
    ''' execute the matches '''
    r = match.start()
    match.save_game_database()
    league.update_domestic_table(r['home_team'], division, season)
    league.update_domestic_table(r['away_team'], division, season)


print(league.get_domestic_cup_table(division, season))
### END SERIE B ###

### SERIE C ###
serie_c_matches = []

competition_name = "Campeonato Brasileiro Série C"
division = 'serie_c'


serie_c_clubs = gene.reconstruct_clubs(division, season)

schedule = gene.define_schedule(serie_c_clubs, stadiums[0]) # the schedule

for club in serie_c_clubs:
    club.set_formation(p_data.get_players(club.name))

for rnd, game_info in schedule.items():
    ''' Defining the schedule '''
    for match in game_info:
        print(match[0].start_eleven)
        serie_c_matches.append(Game(match[0], match[1], competition_name, int(rnd.split(' ')[-1]), season, head_stadium=match[-1]))


tb = rk.domestic_table(division, season) # Get the initial domestic cup table
print(tb) 

for match in serie_c_matches:
    ''' execute the matches '''
    r = match.start()
    match.save_game_database()
    league.update_domestic_table(r['home_team'], division, season)
    league.update_domestic_table(r['away_team'], division, season)


print(league.get_domestic_cup_table(division, season))
### END SERIE C ###