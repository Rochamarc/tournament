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

serie_a = clubs_controller.select_serie_a_clubs()
clubs = cc.clubs(serie_a)
clubs = cc.add_players_to_clubs(clubs, players)

for club in clubs:
    ''' Define the start eleven and the bench '''
    club.start_eleven = formation.starting_eleven(club.squad)
    club.bench = formation.backups(club.squad, club.start_eleven)