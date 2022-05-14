import requests 
import json 

from ..database.database import PlayerData

# player data
p_data = PlayerData()

# links
players_link = "http://localhost:8000/players/" 
clubs_link = "http://localhost:8000/clubs/"

# Getting Clubs
req = requests.get(clubs_link)
clubs = None

if req.status_code == 200:
    clubs = req.content # get the content
    clubs = json.loads(clubs)
else:
    exit()


# data
data = {

}

# headers
headers = {
    'Content-Type': 'application/json'
} 

for club in clubs:
    print(club["name"])
    player = p_data.get_players(club["name"])
    print(player)
    # for i in range()
