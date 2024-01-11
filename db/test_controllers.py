import sys 
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db.main_controller import MainController
from db.player_contracts_controller import PlayerContractsController

# Running tests on controllers

# print(MainController().select_clubs())
# print(MainController().select_competitions())

print(PlayerContractsController().select_players_with_no_contract())
