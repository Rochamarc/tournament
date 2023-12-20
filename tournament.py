from alive_progress import alive_it

from data_helper import prepare_player_stats_to_db
from logs_helper import LogsHandler

from db.championships_controller import ChampionshipsController
from db.games_controller import GamesController
from db.players_controller import PlayersController

logs_handler = LogsHandler()

championships_controller = ChampionshipsController()
games_controller = GamesController()
player_controller = PlayersController()

def run_league(games: list, season: str) -> None:
    """Run a full season of a league tournament

    Parameters
    ----------
    games : list
        A Game object list
    season : str
        A str with season 

    Returns
    -------
        None
    """
    
    for game in alive_it(games):
        game.start()

        # saving into database
        game_stats = logs_handler.get_game_stats(game.logs, game.home, game.away)
        stats_data = logs_handler.prepare_game_stats_logs_to_db(game_stats)

        # Insert and Get the id of the game stats inserted
        home = games_controller.insert_game_stat_with_id_return(stats_data[0])
        away = games_controller.insert_game_stat_with_id_return(stats_data[1])

        # Game stats id
        game_ids = home[0][0], away[0][0]

        # Prepare data for insertiong
        prepare_game = logs_handler.prepare_game_logs_to_db(game.logs, game_ids)
        
        # Get game id
        game_id = games_controller.insert_game(prepare_game)
        game_id = game_id[0][0]

        # prapare players stats per game data
        player_stats = game.logs['stats']
        player_stats_data = prepare_player_stats_to_db(player_stats, season, game_id)

        # insert players stats per game on db
        player_controller.insert_players_stats(player_stats_data)

        # Preapre data to update on db
        home_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.home, season)
        away_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.away, season)

        # update championships on database
        championships_controller.update_championship_table(home_data, game.competition)
        championships_controller.update_championship_table(away_data, game.competition)