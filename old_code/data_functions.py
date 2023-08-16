from db.player_controller import PlayerData

player_data = PlayerData()

def prepare_player_to_player_season(players: list, season: str) -> list:
    ''' Will Remove the extra rows that have in players table and are not necessary in the player_season table '''
    p_season = []
    
    # player of Player() class
    
    for player in players:
        player_data = player.data_season()
        
        # add current season
        player_data.append(season)
        
        p_season.append(player_data)
        
    return p_season

def prepare_player_to_retiring(players: list) -> list:
    ''' Will remove the extra rows that have in players and are not necessary in the retirees table '''
    retirees = []
    
    # prepare the retiree data, exclude the 10, 11, 17, 18 items in the tuple
    for player in players:
        player = list(player)        
        del player[18]
        del player[17]
        del player[0]
        
        retirees.append(player)
        
    return retirees

if __name__ == "__main__":
    print(prepare_player_to_retiring())