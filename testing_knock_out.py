from knock_out import knock_out_match
from classes import Club 

from time import sleep 
from pprint import pprint 

river = Club('River Plate', 'Argentina')
eme = Club('Emelec', 'Ecuador')

river.register_squad(skip_db=True)
river.formation_auto()

eme.register_squad(skip_db=True)
eme.formation_auto()


### Aqui comeca as partidas
quarter_finals = {
    'competition': 'Conmebol Libertadores',
    'game': 1,
    'round': 'Quarter Final',
    'home_team': river,
    'away_team': eme,
    'home_goal': 0,
    'away_goal': 0
}   

quarter = knock_out_match(quarter_finals, verbose=True) # vira um dict

pprint(quarter) # observando as mudancas

sleep(2)

quarter['home_team'], quarter['away_team'] = quarter['away_team'], quarter['home_team']
quarter['home_goal'], quarter['away_goal'] = quarter['away_goal'], quarter['home_goal']
quarter['game'] = 2
 
quarter = knock_out_match(quarter, verbose=True)

pprint(quarter)



final = {
    'competition': 'Conmebol Libertadores',
    'game': 1,
    'round': 'Final',
    'home_team': river,
    'away_team': eme,
    'home_goal': 0,
    'away_goal': 0
}   

final = knock_out_match(final, verbose=True)

pprint(final)
