from classes import Club
from ranking import define_conmebol_points
from group_stage_draw import *
from group_stage import *
from knock_out_draw import define_knock_out_stage
from knock_out import knock_out_match
from pprint import pprint 

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
clubs = []

# Creating a save file
save_file = input("Digite um valor de ate 30 caracteres pra criar um save file: ")

for club, country in ls.items():
    if save_file:
        c = Club(club, country, save_file=save_file)
    else:
        c = Club(club, country)
    c.register_squad(skip_db=True)
    c.formation_auto()

    clubs.append(c)

define_conmebol_points(clubs) # add conmebol points to each correspondent club

qualifying_phase = ['Santos', 'Always Ready','Junior', 'Atlético Nacional', 'Unión La Calera', 'Independiente del Valle', 'Rentistas','Deportivo La Guaira']
try:
    groups = define_group_stage(clubs, qualifying_phase)
except:
    groups = define_group_stage(clubs, qualifying_phase)

a_group = group_stage("A", groups['A'], 'Conmebol Libertadores') #, verbose=True)
b_group = group_stage("B", groups['B'], 'Conmebol Libertadores') #, verbose=True)
c_group = group_stage("C", groups['C'], 'Conmebol Libertadores') #, verbose=True)
d_group = group_stage("D", groups['D'], 'Conmebol Libertadores') #, verbose=True)
e_group = group_stage("E", groups['E'], 'Conmebol Libertadores') #, verbose=True)
f_group = group_stage("F", groups['F'], 'Conmebol Libertadores') #, verbose=True)
g_group = group_stage("G", groups['G'], 'Conmebol Libertadores') #, verbose=True)
h_group = group_stage("H", groups['H'], 'Conmebol Libertadores') #, verbose=True)


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
    idas.append(knock_out_match(d, verbose=True))

pprint(idas)