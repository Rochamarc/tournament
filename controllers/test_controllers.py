import sys 
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controllers.players_controller import PlayersController
from controllers.market_controller import MarketController

class TestPlayers:
    def test_last_players_length(self):
        assert len(PlayersController.select_last_players()) == 30
    
    def test_last_players(self):
        assert PlayersController.select_last_players()

class TestSkills:
    def test_skill_in_skills(self):
        # select the first value on last skills, to check if  
        # the value is on select_skills
        last_skills = PlayersController.select_last_skills('2022')[0]

        assert last_skills in PlayersController.select_skills('2022')  

    def test_values_in_skills(self):
        assert all(PlayersController.select_skills('2022'))

    def test_skill_in_list(self):
        assert PlayersController.select_last_skills('2022')

    def test_compare_last_players_with_last_players(self):
        assert [ i[-1] for i in PlayersController.select_last_skills('2022') ] == [ i[0] for i in PlayersController.select_last_players() ]
    
    def test_len_last_skills(self):
        assert len(PlayersController.select_last_skills('2022')[0]) == 10

class TestMarket:
    def test_search_by_overall_length(self):
        assert len(MarketController.search_by_overall(88, 2022)[0]) == 11
    
    def test_search_by_age_length(self):
        assert len(MarketController.search_by_age(22, 2022)[0]) == 11

    def test_search_by_position_length(self):
        assert len(MarketController.search_by_position('CF', 2022)[0]) == 11
    
    def test_search_by_all_length(self):
        assert len(MarketController.search_by_all('SS', 70, 2022)[0]) == 11