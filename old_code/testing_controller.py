from db.player_controller import PlayerData
from pprint import pprint 


p = PlayerData()

for p in p.get_retiring_players():
    print(p)