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
            l = [ i for i in player ]
            skill = list(skill)
            skill[-1] = 0

            l += skill
            new_list.append(l)

players = class_const.players(new_list)

hashes = [ 
    [ generate_player_hash(player.overall), player.id ] for player in players
]

# for player in players:
#     hash = generate_player_hash(player.overall)
#     value = [ hash, player.id ]
#     hashes.append(value)

# print(hashes)

for hash in hashes:
    hash_string = json.dumps(list(hash[0]))
    # print(type(hash_string))
    player_controller.insert
    exit()