from random import choice
from database import PlayerData

from draw import Draw
from knock_out import KnockOutGame
from classes_helper import GenerateClass

draw = Draw()
generate = GenerateClass()

copa_do_brasil_matches = draw.national_draw()

stadiums = generate.reconstruct_stadiums() 

player_data = PlayerData()

results = []

for match in copa_do_brasil_matches:
    match[0].set_formation(player_data.get_players(match[0].name))
    match[1].set_formation(player_data.get_players(match[1].name))
    
    m_1 = KnockOutGame(match[0], match[1], 'Copa do Brasil', 1, '2021', 'Knock Out', head_stadium=choice(stadiums), verbose=False).first_leg()
    print(m_1)

    results.append(m_1)

print(results)