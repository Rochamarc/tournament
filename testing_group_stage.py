from classes import Club
from ranking import define_conmebol_points
from group_stage_draw import *

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

for club, country in ls.items():
    clubs.append(Club(club, country))

define_conmebol_points(clubs) # add conmebol points to each correspondent club

qualifying_phase = ['Santos', 'Always Ready','Junior', 'Atlético Nacional', 'Unión La Calera', 'Independiente del Valle', 'Rentistas','Deportivo La Guaira']
define_group_stage(clubs, qualifying_phase)

