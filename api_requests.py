import http.client, urllib.parse
import json 
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
    def get_players():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['players'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)
    
    @staticmethod
    def post_players():
        data = get_json_obj('player.json')

        conn = http.client.HTTPConnection(base_link)
        conn.request("POST", base_args['players'], json.dumps(data), headers)

        r = conn.getresponse()

        print(r.read())

        conn.close()

        return None

class CLubAPI:
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

class TrophyAPI:
    @staticmethod
    def get_trophies():
        conn = http.client.HTTPConnection(base_link)
        conn.request("GET", base_args['trophies'])

        r1 = conn.getresponse()
        data = r1.read()

        conn.close()

        return json.loads(data)    

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
    def post_table(table_info):
        conn = http.client.HTTPConnection(base_link)

        for table in table_info:
            conn.request("POST", base_args['tables'], table.data, headers)
            r1 = conn.getresponse()
            print(r1.read())

        conn.close()

        return None    



if __name__ == "__main__":
    from pprint import pprint
    