from helper import ClassConstructor
from db.players_controller import PlayersController
from db.clubs_controller import ClubsController
from classes.formation import Formation

cc = ClassConstructor()
players_controller = PlayersController()
clubs_controller = ClubsController()
formation = Formation()

p = players_controller.select_players_with_contract('2022') # get from db
players = cc.players(p) # transform into objects

# serie a
serie_a = clubs_controller.select_serie_a_clubs()
serie_a_clubs = cc.clubs(serie_a)
serie_a_clubs = cc.add_players_to_clubs(serie_a_clubs, players)

# serie b
serie_b = clubs_controller.select_serie_b_clubs()
serie_b_clubs = cc.clubs(serie_b)
serie_b_clubs = cc.add_players_to_clubs(serie_b_clubs, players)

# serie c
serie_c = clubs_controller.select_serie_c_clubs()
serie_c_clubs = cc.clubs(serie_c)
serie_c_clubs = cc.add_players_to_clubs(serie_c_clubs, players)


for club in serie_a_clubs:
    ''' Define the start eleven and the bench '''
    club.start_eleven = formation.starting_eleven(club.squad)
    club.bench = formation.backups(club.squad, club.start_eleven)


for club in serie_b_clubs:
    ''' Define the start eleven and the bench '''
    club.start_eleven = formation.starting_eleven(club.squad)
    club.bench = formation.backups(club.squad, club.start_eleven)


for club in serie_c_clubs:
    ''' Define the start eleven and the bench '''
    club.start_eleven = formation.starting_eleven(club.squad)
    club.bench = formation.backups(club.squad, club.start_eleven)