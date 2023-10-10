from helper import ClassConstructor
from db.players_controller import PlayersController
from db.clubs_controller import ClubsController
from db.stadiums_controller import StadiumsController


# Static classes
class_const = ClassConstructor()
players_controller = PlayersController()
clubs_controller = ClubsController()
stadiums_controller = StadiumsController()


# Select and transform stadium data into objects
stadiums_data = stadiums_controller.select_all_stadiums()
stadiums = class_const.stadiums(stadiums_data)

# Select players with contract
p = players_controller.select_players_with_contract('2022') # get from db
players = class_const.players(p) # transform into objects

# Serie A clubs selection & cast
serie_a = clubs_controller.select_serie_a_clubs()
serie_a_clubs = class_const.clubs(serie_a)
serie_a_clubs = class_const.add_players_to_clubs(serie_a_clubs, players)

# Serie B clubs selection & cast
serie_b = clubs_controller.select_serie_b_clubs()
serie_b_clubs = class_const.clubs(serie_b)
serie_b_clubs = class_const.add_players_to_clubs(serie_b_clubs, players)

# Serie C clubs selection & cast
serie_c = clubs_controller.select_serie_c_clubs()
serie_c_clubs = class_const.clubs(serie_c)
serie_c_clubs = class_const.add_players_to_clubs(serie_c_clubs, players)

# Set clubs formation
class_const.define_formation(serie_a_clubs)
class_const.define_formation(serie_b_clubs)
class_const.define_formation(serie_c_clubs)

# Define the clubs matches, this will return a list of lists with two differents teams
serie_a_schedule = class_const.define_schedule(serie_a_clubs)
serie_b_schedule = class_const.define_schedule(serie_b_clubs)
serie_c_schedule = class_const.define_schedule(serie_c_clubs)

# Return a list of games object with all the confrontations through the season
serie_a_games = class_const.prepare_games(serie_a_schedule, stadiums, 'Campeonato Brasileiro Serie A', 2022)
serie_b_games = class_const.prepare_games(serie_b_schedule, stadiums, 'Campeonato Brasileiro Serie B', 2022)
serie_c_games = class_const.prepare_games(serie_c_schedule, stadiums, 'Campeonato Brasileiro Serie C', 2022)

# Starting this matches
for game in serie_a_games:
    game.start()

for game in serie_b_games:
    game.start()

for game in serie_c_games:
    game.start()