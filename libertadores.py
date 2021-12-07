from classes_helper import *
from group_stage_draw import *
from ranking import Ranking
from database import InternationalCup

gene = GenerateClass()
rank = Ranking()
gs = GroupStage()
inter = InternationalCup()

season = '2021'

clubs = gene.set_clubs('files/libertadores/2021/clubs.txt') # Generate the 32 clubs
stadiums = gene.set_stadium() # Generate all stadiums
gene.define_clubs_stadium(clubs, stadiums) # 

rank.define_conmebol_points(clubs) 

qualifying_phase = [
        'Santos', 
        'Always Ready',
        'Junior', 
        'Atlético Nacional', 
        'Unión La Calera', 
        'Independiente del Valle', 
        'Rentistas',
        'Deportivo La Guaira'
]

groups = gs.define_group_stage(clubs, qualifying_phase, season) # working
tb = rank.international_group_table('2021')

# group_phase = [ gs.group_stage(key, item, 'Conmebol Libertadores', verbose=True) for key, item in groups.items() ]
# from pprint import pprint

# pprint(group_phase)
