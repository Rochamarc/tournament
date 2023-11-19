from db.championships_controller import ChampionshipsController
from db.clubs_controller import ClubsController
from db.games_controller import GamesController
from db.stadiums_controller import StadiumsController

from data_manipulation import fomrmulate_clubs_to_simple_cup
from helper import ClassConstructor

# Declare my controllers
championships_controller = ChampionshipsController()
games_controller = GamesController()
class_constructor = ClassConstructor()
stadiums_controller = StadiumsController()
clubs_controller = ClubsController()


# Select stadiums 
stadiums_data = stadiums_controller.select_all_stadiums()
stadiums = class_constructor.stadiums(stadiums_data)

# Select clubs from serie a
a = championships_controller.select_serie_a_cup('2022')

# Select 12 random clubs from serie b or c
bc = championships_controller.select_serie_b_c_cup('2022')

# Formulate list with ids
ids = fomrmulate_clubs_to_simple_cup(a,bc)

# Get clubs data
clubs_data = [ clubs_controller.select_club_by_id(i)[0] for i in ids ]

# Get clubs objects
clubs = clubs_controller.clubs(clubs_data)

# Define the condronts
game_data = class_constructor.sort_simple_cup_confronts(clubs)

# Prepare games
class_constructor.prepare_games(game_data, stadiums, 'Copa do Brasil', 2022)