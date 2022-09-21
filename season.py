from classes_helper import GenerateClass
from game import Game
from ranking import Ranking

from api_requests import PlayerAPI, GameAPI, TableAPI
from database import GameData, PlayerData, DomesticLeague

game_api = GameAPI()
player_api = PlayerAPI()
table_api = TableAPI()


gene = GenerateClass()
league = DomesticLeague()
p_data = PlayerData()
game_data = GameData()

rk = Ranking()

stadiums = [ gene.reconstruct_stadiums() ]

class Season:
    def __init__(self, competition, season, division):
        self.competition = competition
        self.season = season
        self.division = division

    def run(self, api=True):
        ''' Run a season '''
        ### SERIE A ###
        matches = []

        clubs = gene.reconstruct_clubs(self.division, self.season) # with this line i get my clubs list of objects

        schedule = gene.define_schedule(clubs, stadiums[0]) # the schedule

        ''' Here we reconstruct the players and formation of the clubs '''
         
        for club in clubs:
            if api:
                club.set_formation(player_api.get_players(club.name))
            else:    
                club.set_formation(p_data.get_players(club.name))

        for rnd, game_info in schedule.items():
            ''' Defining the schedule '''
            for match in game_info:
                print(match[0].start_eleven)
                matches.append(Game(match[0], match[1], self.competition, int(rnd.split(' ')[-1]), self.season, head_stadium=match[-1]))


        tb = rk.domestic_table(self.division, self.season) # Get the initial domestic cup table
        print(tb) 

        for match in matches:
            ''' execute the matches '''
            r = match.start()

            if api:
                table_api.update_table(r['home_team'], self.division, self.season)
                table_api.update_table(r['away_team'], self.division, self.season)
            else:
                league.update_domestic_table(r['home_team'], self.division, self.season)
                league.update_domestic_table(r['away_team'], self.division, self.season)

        tb = rk.domestic_table(self.division, self.season) # Get the initial domestic cup table
        print(tb) 

        # END SEASON

        ''' Upload games stats to the api '''
        if api:
            game_api.post_games(matches)
        else:
            game_data.insert_games_db(matches)

        
        # UPDATE PLAYERS
        for club in clubs:
            p_data.update_player_stats(club.start_eleven, verbose=True)
            p_data.update_player_stats(club.bench, verbose=True)
        
            
        return None