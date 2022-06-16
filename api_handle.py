import requests
import json

from database import CoachData

# api links
base_link = "http://still-wave-44749.herokuapp.com/"

trophies_link = f"{base_link}trophies/"
clubs_link = f"{base_link}clubs/"
game_link = f"{base_link}games/"
coaches_link = f"{base_link}coaches/"


# content info
headers = { 'Content-Type': 'application/json' }

def upload_trophy(club_name, season, competition):
    club = get_club(club_name)

    data = {
        "season": season,
        "competition": competition,
        "club_owner": f"{clubs_link}{club['id']}/"
    }

    requests.post(trophies_link, data=json.dumps(data))

def get_players(club_name):
    ''' Reconstruct the club formation and players '''

    club = get_club(club_name)

    return club['players']
    

def get_clubs(clubs_list):
    ''' Return a list of clubs api data '''
    
    clubs = json.loads(requests.get(clubs_link).content)
    return [ club for club in clubs if club['name'] in clubs_list ]

def get_club(club_name):
    ''' Return the api dict with the club object '''

    clubs = json.loads(requests.get(clubs_link).content)
    
    for club in clubs:
        if club['name'] == club_name : return club


def upload_trophy(club_owner, season, competition):

    club = get_club(club_owner)

    data = {
        "club_owner" : f'{clubs_link}{club["id"]}/',
        "season": season,
        "competition": competition
    }

    r = requests.post(trophies_link, data=json.dumps(data), headers=headers)

    print(r.text)

def upload_game(game_data):
    ''' Upload game data to the api '''
    r = requests.post(game_link, data=json.dumps(game_data), headers=headers)

    print(r.text)


def upload_coaches():
    coach_data = CoachData()
    coaches = coach_data.get_all_coaches()

    for coach in coaches:
        club = get_club(coach[-1])
        club_id = club["id"]

        # my data
        data = {
                "name": coach[1],
                "nationality": coach[2],
                "age": coach[3],
                "formation": coach[4],
                "play_mode": coach[5],
                "current_club": f"{clubs_link}{club_id}/"
        }

        r = requests.post(coaches_link, data=json.dumps(data), headers=headers)

    
        print(r.text)
        

    return True

if __name__ == "__main__":
    upload_trophy('Palmeiras', '2021', 'Conmebol Libertadores')