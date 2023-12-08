from helper import ClassConstructor
from db.champions_controller import ChampionsController
from db.championships_controller import ChampionshipsController
from db.competitions_controller import CompetitionsController
from db.clubs_controller import ClubsController
from db.games_controller import GamesController
from db.players_controller import PlayersController
from db.stadiums_controller import StadiumsController

from tournament import run_league

from data_manipulation import formulate_clubs_to_championships, relegate_serie_a, relegate_serie_b, relegate_serie_c

from logs_helper import LogsHandler

from alive_progress import alive_it

# TODO nao ta atualizando o championships 
#
#

# define a season

season = '2022'

# Static classes
class_const = ClassConstructor()

champions_controller = ChampionsController()
championships_controller = ChampionshipsController()
competitions_controller = CompetitionsController()
clubs_controller = ClubsController()
games_controller = GamesController()
players_controller = PlayersController()
stadiums_controller = StadiumsController()

logs_handler = LogsHandler()

# Select and transform stadium data into objects
stadiums_data = stadiums_controller.select_all_stadiums()
stadiums = class_const.stadiums(stadiums_data)

# Select players with contract
players_data = players_controller.select_players_with_contract(season)

competition_name = 'Campeonato Brasileiro'
competition_id = competitions_controller.select_competition_id(competition_name)[0][0]

# Promoted and relegate
promo = input("Want to promote and relegate [Y/n]: ")

if promo in ['Y','y']:
    print("Promoting and relegating clubs")

    season = str(int(season) + 1)

    # select from championships
    a = championships_controller.select_championships_to_insert('Serie A')
    b = championships_controller.select_championships_to_insert('Serie B')
    c = championships_controller.select_championships_to_insert('Serie C')

    a = relegate_serie_a(a, season)
    b = relegate_serie_b(b, season)
    c = relegate_serie_c(c, season)

    # formulate data
    serie_a = formulate_clubs_to_championships(a['remains'],b['promoted'], [])
    serie_b = formulate_clubs_to_championships(a['relegated'],b['remains'], c['promoted'])
    serie_c = formulate_clubs_to_championships(b['relegated'],c['remains'], [])

    # Creates next season default
    championships_controller.insert_championship(serie_a)
    championships_controller.insert_championship(serie_b)
    championships_controller.insert_championship(serie_c)


# Serie A clubs selection & cast
serie_a = clubs_controller.select_serie_a_clubs(season)
serie_a_clubs = class_const.prepare_clubs(serie_a, players_data)

# Serie B clubs selection & cast
serie_b = clubs_controller.select_serie_b_clubs(season)
serie_b_clubs = class_const.prepare_clubs(serie_b, players_data)

# Serie C clubs selection & cast
serie_c = clubs_controller.select_serie_c_clubs(season)
serie_c_clubs = class_const.prepare_clubs(serie_c, players_data)

# Define the clubs matches, this will return a list of lists with two differents teams
serie_a_schedule = class_const.define_schedule(serie_a_clubs)
serie_b_schedule = class_const.define_schedule(serie_b_clubs)
serie_c_schedule = class_const.define_schedule(serie_c_clubs)

# Return a list of games object with all the confrontations through the season
serie_a_games = class_const.prepare_games(serie_a_schedule, stadiums, competition_name, competition_id, int(season))
serie_b_games = class_const.prepare_games(serie_b_schedule, stadiums, competition_name, competition_id, int(season))
serie_c_games = class_const.prepare_games(serie_c_schedule, stadiums, competition_name, competition_id, int(season))


print("Running serie A")
run_league(serie_a_games, season)

print("Running serie B")
run_league(serie_b_games, season)
 
print("Running serie C")
run_league(serie_c_games, season)


# insert champions 
a_champion = championships_controller.select_champion(season, 'Serie A')[0]
b_champion = championships_controller.select_champion(season, 'Serie B')[0]
c_champion = championships_controller.select_champion(season, 'Serie C')[0]

champions_controller.insert_champion(a_champion[0],a_champion[1],a_champion[2])
champions_controller.insert_champion(b_champion[0],b_champion[1],b_champion[2])
champions_controller.insert_champion(c_champion[0],c_champion[1],c_champion[2])