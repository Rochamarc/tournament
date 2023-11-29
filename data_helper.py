def prepare_player_stats_to_db(player_stats: dict, season: int, game_id: int) -> list[list]:
    """Prepare a list of data to insert into tournament.stats schema

    Parameters
    ----------
    player_stats : dict
        Stats from Game.logs['stats'] format
    game_id : int
        A integer of the id from the game

    Returns
    -------
        A list of list with tournament.stats data
    """
    player_data = []

    for _, item in player_stats.items():
        data = [
            season,
            item['matches'],
            item['shots'],
            item['shots_on_target'],
            item['goals'],
            item['assists'],
            item['fouls_committed'],
            item['tackles'],
            item['passes'],
            item['wrong_passes'],
            item['intercepted_passes'],
            item['clearances'],
            item['stolen_balls'],
            item['clean_sheets'],
            item['defenses'],
            item['difficult_defenses'],
            item['goals_conceded'],
            item['player_id'],
            game_id
        ]

        player_data.append(data)

    return player_data