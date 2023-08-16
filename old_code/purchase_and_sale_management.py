from random import choice 
from db.player_controller import PlayerData
from helper import Helper
from alive_progress import alive_bar

player_data = PlayerData()
helper = Helper()

class PlayerManagement:
    @staticmethod
    def retirement_decision(clubs_list: list) -> None:
        ''' 
        Get a list of clubs, capture all of his players and will decide if the players of 
        33y/o or higher if the player will retire and save on database. 
        '''

        players = helper.get_players_list(clubs_list)        
        update_players = []
        
        print('Updating players with 33 years old or higher')
        with alive_bar(len(players)) as bar:
            for player in players:
                player.retirement = choice(['True','False']) if player.age >= 33 else 'False' # update retirement variable
                if player.retirement == 'True':
                    update_players.append(player) # add to database update
                bar()
        
        print('Updating 33 years old or higher on database')
        with alive_bar(len(update_players)) as bar:
            player_data.update_players_retirement(update_players)
            bar()
        
        return None
                    
    
            
        
        
        
    