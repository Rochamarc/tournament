import requests 
import json 

from database import PlayerData

# player data
p_data = PlayerData()

# links
players_link =  "http://still-wave-44749.herokuapp.com/players/"
clubs_link = "http://still-wave-44749.herokuapp.com/clubs/"

# Getting Clubs
req = requests.get(clubs_link)
clubs = None

if req.status_code == 200:
    clubs = req.content # get the content
    clubs = json.loads(clubs)
else:
    exit()


# headers
headers = { 'Content-Type': 'application/json'}

for club in clubs:
    players = p_data.get_players(club["name"])
    for player in players:

        player = tuple(player)
        print(player)

        # player data
        data = {
            "name": player[1],
            "nationality": player[2],
            "age": player[3],
            "overall": player[4],
            "current_club": f'{clubs_link}{club["id"]}/',
            "position": player[6],
        }

        print(data)

        r = requests.post(players_link, data=json.dumps(data), headers=headers)

        print(r.text)
