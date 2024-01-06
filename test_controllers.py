# Running tests on controllers

from db.main_controller import MainController

print(MainController().select_clubs())
print(MainController().select_competitions())