from helper import ClassConstructor
from db.players_controller import PlayersController
from db.clubs_controller import ClubsController
from db.stadiums_controller import StadiumsController
from classes.formation import Formation
from game import Game 

def define_formation(clubs: list) -> None:
    for club in clubs:
        club.start_eleven = formation.starting_eleven(club.squad)
        club.bench = formation.backups(club.squad, club.start_eleven)

def define_schedule(clubs_list: list):
    games = []
    for home in clubs_list:
        for away in clubs_list:
            if home != away : games.append([home, away]) 
    return games

def prepare_games(games: list, competition: str, season: int) -> list[Game]:
    pass 


class_const = ClassConstructor()
players_controller = PlayersController()
clubs_controller = ClubsController()
stadiums_controller = StadiumsController()
formation = Formation()

p = players_controller.select_players_with_contract('2022') # get from db
players = class_const.players(p) # transform into objects

# serie a clubs
serie_a = clubs_controller.select_serie_a_clubs()
serie_a_clubs = class_const.clubs(serie_a)
serie_a_clubs = class_const.add_players_to_clubs(serie_a_clubs, players)

# serie b clubs
serie_b = clubs_controller.select_serie_b_clubs()
serie_b_clubs = class_const.clubs(serie_b)
serie_b_clubs = class_const.add_players_to_clubs(serie_b_clubs, players)

# serie c clubs
serie_c = clubs_controller.select_serie_c_clubs()
serie_c_clubs = class_const.clubs(serie_c)
serie_c_clubs = class_const.add_players_to_clubs(serie_c_clubs, players)

# this will set the clubs start eleven and bench
define_formation(serie_a_clubs)
define_formation(serie_b_clubs)
define_formation(serie_c_clubs)

serie_a_schedule = define_schedule(serie_a_clubs)
serie_b_schedule = define_schedule(serie_b_clubs)
serie_c_schedule = define_schedule(serie_c_clubs)

stadiums_data = stadiums_controller.select_all_stadiums()
stadiums = class_const.stadiums(stadiums_data)

