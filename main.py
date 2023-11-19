from helper import ClassConstructor
from db.champions_controller import ChampionsController
from db.championships_controller import ChampionshipsController
from db.clubs_controller import ClubsController
from db.games_controller import GamesController
from db.players_controller import PlayersController
from db.stadiums_controller import StadiumsController

from data_manipulation import formulate_clubs_to_championships, relegate_serie_a, relegate_serie_b, relegate_serie_c

from logs_helper import LogsHandler


# define a season

season = '2022'

# Static classes
class_const = ClassConstructor()

champions_controller = ChampionsController()
championships_controller = ChampionshipsController()
clubs_controller = ClubsController()
games_controller = GamesController()
players_controller = PlayersController()
stadiums_controller = StadiumsController()

logs_handler = LogsHandler()

# Select and transform stadium data into objects
stadiums_data = stadiums_controller.select_all_stadiums()
stadiums = class_const.stadiums(stadiums_data)

# Select players with contract
p = players_controller.select_players_with_contract(season) # get from db
players = class_const.players(p) # transform into objects


# Promoted and relegate

promo = input("Want to promote and relegate [Y/n]: ")

if promo in ['Y','y']:
    print("Promoting and relegating clubs")

    season = str(int(season) + 1)

    # select from championships
    a = championships_controller.select_championships_to_insert('Serie A')
    b = championships_controller.select_championships_to_insert('Serie B')
    c = championships_controller.select_championships_to_insert('Serie C')

    a = relegate_serie_a(a, season)
    b = relegate_serie_b(b, season)
    c = relegate_serie_c(c, season)

    # formulate data
    serie_a = formulate_clubs_to_championships(a['remains'],b['promoted'], [])
    serie_b = formulate_clubs_to_championships(a['relegated'],b['remains'], c['promoted'])
    serie_c = formulate_clubs_to_championships(b['relegated'],c['remains'], [])

    # Creates next season default
    championships_controller.insert_championship(serie_a)
    championships_controller.insert_championship(serie_b)
    championships_controller.insert_championship(serie_c)


# Serie A clubs selection & cast
serie_a = clubs_controller.select_serie_a_clubs(season)
serie_a_clubs = class_const.clubs(serie_a)
serie_a_clubs = class_const.add_players_to_clubs(serie_a_clubs, players)

# Serie B clubs selection & cast
serie_b = clubs_controller.select_serie_b_clubs(season)
serie_b_clubs = class_const.clubs(serie_b)
serie_b_clubs = class_const.add_players_to_clubs(serie_b_clubs, players)

# Serie C clubs selection & cast
serie_c = clubs_controller.select_serie_c_clubs(season)
serie_c_clubs = class_const.clubs(serie_c)
serie_c_clubs = class_const.add_players_to_clubs(serie_c_clubs, players)

# Set clubs formation
class_const.define_formation(serie_a_clubs)
class_const.define_formation(serie_b_clubs)
class_const.define_formation(serie_c_clubs)

# Define the clubs matches, this will return a list of lists with two differents teams
serie_a_schedule = class_const.define_schedule(serie_a_clubs)
serie_b_schedule = class_const.define_schedule(serie_b_clubs)
serie_c_schedule = class_const.define_schedule(serie_c_clubs)

# Return a list of games object with all the confrontations through the season
serie_a_games = class_const.prepare_games(serie_a_schedule, stadiums, 'Campeonato Brasileiro Serie A', int(season))
serie_b_games = class_const.prepare_games(serie_b_schedule, stadiums, 'Campeonato Brasileiro Serie B', int(season))
serie_c_games = class_const.prepare_games(serie_c_schedule, stadiums, 'Campeonato Brasileiro Serie C', int(season))


print("Running serie A")

# Starting this matches
for game in serie_a_games:
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
    games_controller.insert_games_list([prepare_game])

    home_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.home, season)
    away_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.away, season)

    championships_controller.update_championship_table(home_data)
    championships_controller.update_championship_table(away_data)


print("Running serie B")

for game in serie_b_games:
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
    games_controller.insert_games_list([prepare_game])

    home_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.home, season)
    away_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.away, season)

    championships_controller.update_championship_table(home_data)
    championships_controller.update_championship_table(away_data)


print("Running serie C")


for game in serie_c_games:
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
    games_controller.insert_games_list([prepare_game])

    home_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.home, season)
    away_data = logs_handler.prepare_championships_logs_to_db(game.logs, game.away, season)

    championships_controller.update_championship_table(home_data)
    championships_controller.update_championship_table(away_data)

# insert champions 
a_champion = championships_controller.select_champion(season, 'Serie A')[0]
b_champion = championships_controller.select_champion(season, 'Serie B')[0]
c_champion = championships_controller.select_champion(season, 'Serie C')[0]

champions_controller.insert_champion(a_champion[0],a_champion[1],a_champion[2])
champions_controller.insert_champion(b_champion[0],b_champion[1],b_champion[2])
champions_controller.insert_champion(c_champion[0],c_champion[1],c_champion[2])