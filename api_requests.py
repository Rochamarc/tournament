import http.client, urllib.parse
import json
from game import Game 
from opening import get_json_obj


base_link = "still-wave-44749.herokuapp.com"

base_args = {
    "players": "/players/",
    "clubs": "/clubs/",
    "games": "/games/",
    "coaches": "/coaches/",
    "trophies": "/trophies/",
    "individual_trophies": "/individual_trophies/",
    "season_individual_player_stats": "/season_individual_player_stats/",
    "tables": "/tables/",
}

headers = {
    'Content-Type': 'application/json'
}

class PlayerAPI:
    @staticmethod
    def get_players(club_name):
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['players'])

        r1 = conn.getresponse()
        data = json.loads(r1.read())

        conn.close()
        
        return [ player for player in data if player['current_club']['name'] == club_name ]
            
    @staticmethod
    def post_players(players):
        conn = http.client.HTTPConnection(base_link)

        for player in players:
            conn.request("POST", base_args['players'], json.dumps(player.data), headers)
            r1 = conn.getresponse()
            print(r1.read())

        conn.close()

        return None


class ClubAPI:
    @staticmethod
    def get_clubs():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['clubs'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)    
    
    @staticmethod
    def get_club(id):
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", f"{base_args['clubs']}{id}/")

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)

    @staticmethod
    def get_club_by_name(name):
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", f"{base_args['clubs']}")

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        data = json.loads(data)

        for i in data:
            if i['name'] == name:
                return i

    @staticmethod
    def post_clubs(clubs):
        conn = http.client.HTTPConnection(base_link)

        for club in clubs:
            conn.request("POST", base_args['clubs'], json.dumps(club.data), headers)
            r1 = conn.getresponse()
            response = json.loads(r1.read())
            club.id = response['id']
            print(response)

        conn.close()

        return None
                
class GameAPI:
    @staticmethod
    def get_games():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['games'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)
    
    @staticmethod
    def post_games(games):
        conn = http.client.HTTPConnection(base_link)

        for game in games:
            conn.request("POST", base_args['games'], json.dumps(game.data), headers)
            r1 = conn.getresponse()
            print(r1.read())

        conn.close()

        return None

class CoachAPI:
    @staticmethod
    def get_coaches():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['coaches'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)    
    
    @staticmethod
    def post_coaches(coaches):
        conn = http.client.HTTPConnection(base_link)

        for coach in coaches:
            conn.request("POST", base_args['coaches'], json.dumps(coach.data), headers)
            r1 = conn.getresponse()
            print(r1.read())

        conn.close()

        return None

class TrophyAPI:
    @staticmethod
    def get_trophies():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['trophies'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)    

    @staticmethod
    def post_trophy(season, competition, club):
        conn = http.client.HTTPConnection(base_link)
        
        data = {
            "season": season,
            "competition": competition,
            "club_owner": f"{base_args['clubs']}{club.id}/"
        }

        conn.request("POST", base_args['trophies'], json.dumps(data), headers)
        r1 = conn.getresponse()
        print(r1.read())

        conn.close()

        return None

class TableAPI:
    @staticmethod
    def get_tables():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['tables'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)

    @staticmethod
    def post_tables(clubs, competition, season):
        conn = http.client.HTTPConnection(base_link)

        for club in clubs:
            data = {
                "season": season,
                "competition": competition,
                "club": f"http://still-wave-44749.herokuapp.com/clubs/{club.id}/",
                "points": 0,
                "matches_played": 0,
                "won": 0,
                "draw": 0,
                "lost": 0,
                "goals_for": 0,
                "goals_against": 0,
                "goals_diff": 0
            }

            conn.request("POST", base_args['tables'], json.dumps(data), headers)
            r1 = conn.getresponse()
            print(r1.read())

        conn.close()

        return None    

    @staticmethod
    def update_table(table_info):
        ''' This is probably not working '''
        conn = http.client.HTTPConnection(base_link)

        for table in table_info:
            conn.request("PUT", f"{base_args['tables']}{table['id']}/", table.data, headers)
            r1 = conn.getresponse()
            print(r1.read())

        conn.close()

        return None    


if __name__ == "__main__":
    from pprint import pprint
    