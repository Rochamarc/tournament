from typing import Union

from fastapi import FastAPI

from db.clubs_controller import ClubsController
from db.players_controller import PlayersController

clubs_controller = ClubsController()
players_controller = PlayersController()

app = FastAPI()

@app.get("/serie_a_clubs/{season}")
def read_clubs(season: str):
    data = clubs_controller.select_serie_a_clubs(season)
    return [ dict(zip(['id','club','country','division'], d)) for d in data ]

@app.get("/players/{season}")
def read_players(season: str):
    data = players_controller.select_players_with_contract(season)
    keys = ['id', 'name','country','birth','position','height','weight', 'foot', 'positioning', 'reflexes', 'diving', 'standing_tackle', 'physical', 'passing', 'dribbling', 'long_shot', 'finishing' ]
    return [ dict(zip(keys, d)) for d in data ]