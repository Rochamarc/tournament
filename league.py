from classes_helper import GenerateClass
from game import Game
from ranking import Ranking
from table import Table

from db.game_controller import GameData
from db.player_controller import PlayerData 
from db.domestic_league_controller import DomesticLeague


gene = GenerateClass()
league_data = DomesticLeague()
p_data = PlayerData()
game_data = GameData()

rk = Ranking()

table = Table()

stadiums = [ gene.reconstruct_stadiums() ]

class League:
    def __init__(self, competition, season, division):
        self.competition = competition
        self.season = season
        self.division = division

    def run(self) -> None:
        ''' Run a season '''
        clubs = gene.reconstruct_clubs(self.division, self.season) # with this line i get my clubs list of objects
        schedule = table.define_schedule(clubs, stadiums[0]) # the schedule

        ''' Here we reconstruct the players and formation of the clubs '''
         
        for club in clubs : club.set_formation(p_data.get_players(club.name)) # setting formation

        matches = ( Game(match[0], match[1], self.competition, int(rnd.split(' ')[-1]), self.season, head_stadium=match[-1]) for rnd, game_info in schedule.items() for match in game_info ) # generator
        
        tb = rk.domestic_table(self.division, self.season) # Get the initial domestic cup table
        print(tb) 

        for match in matches:
            ''' execute the matches '''
            r = match.start()

            league_data.update_domestic_table(r['home_team'], self.division, self.season)
            league_data.update_domestic_table(r['away_team'], self.division, self.season)

        tb = rk.domestic_table(self.division, self.season) # Get the initial domestic cup table
        print(tb) 

        # END SEASON
 
        game_data.insert_games_db(matches)
        
        # UPDATE PLAYERS
        for club in clubs:
            p_data.update_player_stats(club.start_eleven, verbose=True) # Update stats
            p_data.update_player_stats(club.bench, verbose=True) # Update Stats
            p_data.update_players_age(club.start_eleven + club.bench, verbose=True) # Update Age
            
        return None