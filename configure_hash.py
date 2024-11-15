import json

from helper import ClassConstructor

from controllers.players_controller import PlayersController
from decision_maker import generate_player_hash

class_const = ClassConstructor()
player_controller = PlayersController()

players = player_controller.select_players()
players_skills = player_controller.select_skills('2022')

new_list = []

for player in players:
    for skill in players_skills:
        if player[0] == skill[-1]:
            data = [ att for att in player ]
            
            skill = list(skill)
            skill[-1] = 0

            data += skill
            new_list.append(data)

players = class_const.players(new_list)

hashes = [ 
    [ json.dumps(list(generate_player_hash(player.overall))), player.id ] for player in players
]

player_controller.insert_player_hashes(hashes)
