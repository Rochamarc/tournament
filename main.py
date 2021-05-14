from classes_helper import *
from group_stage_draw import *
from group_stage import group_stage
from ranking import Ranking

gene = GenerateClass()
rank = Ranking()
gs = GroupStage()

clubs = gene.set_clubs() # Generate the 32 clubs
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

groups = gs.define_group_stage(clubs, qualifying_phase)
group_phase = [ gs.group_stage(key, item, 'Conmebol Libertadores', verbose=True) for key, item in groups.items() ]
from pprint import pprint

pprint(group_phase)
