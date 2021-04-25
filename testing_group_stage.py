from classes import Club
from ranking import define_conmebol_points
from group_stage_draw import *
from group_stage import *

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
    c.register_squad()
    c.formation_auto()

    clubs.append(c)

define_conmebol_points(clubs) # add conmebol points to each correspondent club

qualifying_phase = ['Santos', 'Always Ready','Junior', 'Atlético Nacional', 'Unión La Calera', 'Independiente del Valle', 'Rentistas','Deportivo La Guaira']
try:
    groups = define_group_stage(clubs, qualifying_phase, verbose=True)
except:
    groups = define_group_stage(clubs, qualifying_phase, verbose=True)

    
a_group = group_stage("A", groups['A'], 'Conmebol Libertadores', verbose=True)
b_group = group_stage("B", groups['B'], 'Conmebol Libertadores', verbose=True)
c_group = group_stage("C", groups['C'], 'Conmebol Libertadores', verbose=True)
d_group = group_stage("D", groups['D'], 'Conmebol Libertadores', verbose=True)
e_group = group_stage("E", groups['E'], 'Conmebol Libertadores', verbose=True)
f_group = group_stage("F", groups['F'], 'Conmebol Libertadores', verbose=True)
g_group = group_stage("G", groups['G'], 'Conmebol Libertadores', verbose=True)
h_group = group_stage("H", groups['H'], 'Conmebol Libertadores', verbose=True)


print(a_group)
print(b_group)
print(c_group)
print(d_group)
print(e_group)
print(f_group)
print(g_group)
print(h_group)
