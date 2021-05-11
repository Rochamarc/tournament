
from group_stage_draw import *
from group_stage import *
from knock_out_draw import define_knock_out_stage
from knock_out import *
from pprint import pprint 
from classes_helper import *
from game import *
from ranking import * 


gener = GenerateClass()
r = Ranking()

ls = {
    "Palmeiras": "Brasil",
    "Defensa y Justicia": "Argentina",
    "Universitario de Deportes": "Peru",
    "Independiente del Valle": "Ecuador",
    "Olimpia": "Paraguay",
    "Internacional": "Brasil",
    "Deportivo Táchira": "Venezuela",
    "Always Ready": "Bolivia",
    "Boca Juniors": "Argentina",
    "Barcelona de Guayaquil": "Ecuador",
    "The Strongest": "Bolivia",
    "Santos": "Brasil",
    "River Plate": "Argentina",
    "Independiente Santa Fe": "Colombia",
    "Fluminense": "Brasil",
    "Junior": "Colombia",
    "São Paulo": "Brasil",
    "Racing Club": "Argentina",
    "Sporting Cristal": "Peru",
    "Rentistas": "Uruguay",
    "Nacional": "Uruguay",
    "Universidad Católica": "Chile",
    "Argentinos Juniors": "Argentina",
    "Atlético Nacional": "Colombia",
    "Flamengo": "Brasil",
    "LDU Quito": "Ecuador",
    "Vélez Sarsfield": "Argentina",
    "Unión La Calera": "Chile",
    "Cerro Porteño": "Argentina",
    "Atlético Mineiro": "Brasil",
    "América de Cali": "Colombia",
    "Deportivo La Guaira": "Venezuela"
}


maraca = Stadium('Maracana', 'Rio de Janeiro, Brasil')
clubs = gener.set_clubs(ls)

'''
g = KnockOutGame(clubs[0], clubs[1], 'Conmebol Liberadores', 1, 'Round of 16', maraca)

result = g.first_leg()
result = g.second_leg()
pprint(result)


print(g.total_home)
print(g.total_away)

# print(inspect.get(result = g.second_leg() 
# print(result)

'''

"""
g = KnockOutGame(clubs[0], clubs[1], 'Conmebol Liberadores', 1, 'Final', maraca)
r = g.first_leg()
print(r)
"""


r.define_conmebol_points(clubs) # add conmebol points to each correspondent club

qualifying_phase = ['Santos', 'Always Ready','Junior', 'Atlético Nacional', 'Unión La Calera', 'Independiente del Valle', 'Rentistas','Deportivo La Guaira']

# Define the group stage draw
groups = define_group_stage(clubs, qualifying_phase)

group_phase = []
for key, item in groups.items():
    g = group_stage(key, item, 'Conmebol Libertadores', verbose=True)
    group_phase.append(g)

pprint(group_phase)



"""
a_group = group_stage("A", groups['A'], 'Conmebol Libertadores') #, verbose=True)
b_group = group_stage("B", groups['B'], 'Conmebol Libertadores') #, verbose=True)
c_group = group_stage("C", groups['C'], 'Conmebol Libertadores') #, verbose=True)
d_group = group_stage("D", groups['D'], 'Conmebol Libertadores') #, verbose=True)
e_group = group_stage("E", groups['E'], 'Conmebol Libertadores') #, verbose=True)
f_group = group_stage("F", groups['F'], 'Conmebol Libertadores') #, verbose=True)
g_group = group_stage("G", groups['G'], 'Conmebol Libertadores') #, verbose=True)
h_group = group_stage("H", groups['H'], 'Conmebol Libertadores') #, verbose=True)

# Classified clubs to next round
classified_groups = {
    'first': [
        a_group['first place'],
        b_group['first place'],
        c_group['first place'],
        d_group['first place'],
        e_group['first place'],
        f_group['first place'],
        g_group['first place'],
        h_group['first place'],
    ],
    'second': [
        a_group['second place'],
        b_group['second place'],
        c_group['second place'],
        d_group['second place'],
        e_group['second place'],
        f_group['second place'],
        g_group['second place'],
        h_group['second place'],
    ]
}

round_of_16 = define_knock_out_stage(classified_groups, 'Round of 16') # defined confrontations

pprint(round_of_16)
cont = input("Continue...")

# ida
idas = []

for i in range(len(round_of_16)):
    d = {
        'home_team': round_of_16[f'confrontation {i}'][0],
        'away_team': round_of_16[f'confrontation {i}'][-1],
        'game': 1,
        'round': 'Round of 16',
        'competition': 'Conmebol Libertadores',
        'home_goal': 0,
        'away_goal': 0
    }
    idas.append(knock_out_match(d))

pprint(idas)

best_player = players_podium(clubs, 'Best Player', '2021', save_file=save_file)
top_scorer = players_podium(clubs, 'Top Scorer', '2021', save_file=save_file)
assist = players_podium(clubs, 'Assists', '2021', save_file=save_file)

print(best_player)
print(top_scorer)
print(assist)
"""