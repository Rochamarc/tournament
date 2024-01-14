import sys 
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controllers.skills_controller import SkillsController
from controllers.players_controller import PlayersController

class TestPlayers:
    def test_last_players_length(self):
        assert len(PlayersController.select_last_players()) == 30
    
    def test_last_players(self):
        assert PlayersController.select_last_players()

class TestSkills:
    def test_skill_in_skills(self):
        last_skills = (0, 0, 0, 53, 58, 59, 52, 54, 54, 5256)
        assert last_skills in SkillsController.select_skills('2022')  

    def test_values_in_skills(self):
        assert all(SkillsController.select_skills('2022'))

    def test_skill_in_list(self):
        assert SkillsController.select_last_skills('2022')

    def test_compare_last_players_with_last_players(self):
        assert [ i[-1] for i in SkillsController.select_last_skills('2022') ] == [ i[0] for i in PlayersController.select_last_players() ]
    
    def test_len_last_skills(self):
        assert len(SkillsController.select_last_skills('2022')[0]) == 10