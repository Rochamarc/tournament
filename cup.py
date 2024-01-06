from db.championships_controller import ChampionshipsController
from db.clubs_controller import ClubsController
from db.games_controller import GamesController
from db.stadiums_controller import StadiumsController
from db.players_controller import PlayersController
from db.qualifiers_controller import QualifiersController

from logs_helper import LogsHandler
from data_manipulation import fomrmulate_clubs_to_simple_cup
from helper import ClassConstructor, CupHelper

# Declare my controllers
championships_controller = ChampionshipsController()
clubs_controller = ClubsController()
games_controller = GamesController()
players_controller = PlayersController()
stadiums_controller = StadiumsController()
qualifiers_controller = QualifiersController()

logs_handler = LogsHandler()

class_constructor = ClassConstructor()
cup_helper = CupHelper()

initial_season = '2022'
competition_name = 'Copa do Brasil'

copa_do_brasil_id = 3

# Select stadiums 
stadiums_data = stadiums_controller.select_all_stadiums()
stadiums = class_constructor.stadiums(stadiums_data)

# Select clubs from serie a
a = championships_controller.select_serie_a_cup(initial_season)

# Select 12 random clubs from serie b or c
bc = championships_controller.select_serie_b_c_cup(initial_season)

# Formulate list with ids of clubs that will player the cup
ids = fomrmulate_clubs_to_simple_cup(a,bc)

qualifiers_controller.insert_qualifiers(initial_season, ids, 'Round of 32', copa_do_brasil_id)

# The next 8 lines are all about clubs & players config before they can play the game
clubs_data = [ clubs_controller.select_club_by_id(i)[0] for i in ids ] # Get clubs data
players_data = players_controller.select_players_with_contract(initial_season) # Get players from database

# Prepare clubs
clubs = class_constructor.prepare_clubs(clubs_data, players_data)

# First leg of round of 32
game_data = cup_helper.sort_simple_cup_confronts(clubs) # Define the condronts
games = class_constructor.prepare_cup_games(game_data, competition_name, copa_do_brasil_id, initial_season, 'Round of 32', 1, stadiums)

# this data is used to prepared the inverted confronts
rnd_32 = cup_helper.run_cup_phase('Round of 32', 1, games, 3)


# Invert confronts and prepare a new confronts with inverted home & away
games = cup_helper.invert_confronts(rnd_32, competition_name, copa_do_brasil_id, initial_season, 'Round of 32', 2, stadiums)

rnd_32 = cup_helper.run_cup_phase('Round of 32', 2, games, 3)

# TODO i can acess all the club.id from this rnd_32 varible
# and can restart the process by running all the phases that are missing
# Before that of course, we have to insert this clubs into database on qualifiers for the round of 16 phase
# and also create a check for the qualifiers with this season, phase, match_number and competition