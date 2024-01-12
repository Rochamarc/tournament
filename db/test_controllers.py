import sys 
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db.skills_controller import SkillsController
from db.players_controller import PlayersController

class TestPlayers:
    def test_last_players(self):
        assert len(PlayersController.select_last_players()) == 30


class TestSkills:
    def test_skill_in_skills(self):
        last_skills = (0, 0, 0, 53, 58, 59, 52, 54, 54, 5256)
        assert last_skills in SkillsController().select_skills('2022')  

    def test_values_in_skills(self):
        assert all(SkillsController().select_skills('2022'))