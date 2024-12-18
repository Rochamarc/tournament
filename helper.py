from classes.club import Club
from classes.formation import Formation
from classes.player import Player
from classes.stadium import Stadium

from controllers.games_controller import GamesController

from logs_helper import LogsHandler

from game import Game 
from cup_game import CupGame

from random import choice, shuffle


games_controller = GamesController()
logs_handler = LogsHandler()

formation = Formation()

class ClassConstructor:
	"""
    Class focused in transform db data into objects


    Methods
    -------
    players(players_data: list)
        Instantiate players
   	clubs(clubs_data: list)
		Instantiate clubs
	stadiums(stadiums_data: list)
		Instantiate stadiums
	add_players_to_clubs(clubs: list, players: list)
		Add players to Club.squad
	define_formation(clubs: list)
		Modify Club's start_eleven and bench
	define_schedule(clubs: list)
		Generates confronts between clubs
	prepare_games(games: list, stadiums: list, competition: str, season: int)
		Instantiate games
	prepare_cup_games(games: list, competition: str, competition_id: int, season: str, phase: str, game_number: int, stadiums: list, first_leg_home_goals: int=0, first_leg_away_goals: int=0)
		Instantiate cup games
	prepare_clubs(cls, clubs_data: list, players_data: list)
		Instantiate clubs & players and configure their formation
	"""
    
	@staticmethod
	def players(players_data: list) -> list[Player]:	
		"""Transform data into Player Objects
		
		Parameters
		----------
		players_data : list
			A list of data with the following format
			[ id, name, nationality, birth, position, height, weight, foot, positioning,
			reflexes, diving, dribling, long_shot, finishing, club_id ]
		
		Returns
		-------
			A list of Player Objects constructed with the data received
		"""

		return [ Player(*pd) for pd in players_data ]

	@staticmethod
	def clubs(clubs_data: list) -> list[Club]:
		"""Transform data into Club Objects
		
		Parameters
		----------
		clubs_data : list
			A list of data with the following format 
			[ club_id, club_name, club_country ] 
		
		Returns
		-------
			A list of Club Objects constructed with the data received
		"""

		return [ Club(*cd[:-1]) for cd in clubs_data ]
	
	@staticmethod
	def stadiums(stadiums_data: list) -> list[Stadium]:
		"""Transform data into Stadium Objects 
		
		Parameters
		----------
		stadiums_data : list
			A list of data with the following format 
			[ stadium_name, stadium_country, stadium_city, stadium_capacity ] 
		
		Returns
		-------
			A list of Stadium Objects constructed with the data received
		"""

		return [ Stadium(*sd) for sd in stadiums_data ] 
	

	@staticmethod
	def add_players_to_clubs(clubs: list, players: list) -> list[Club]:
		"""Add players to squad according to player.club_id and club_id
		
		Parameters
		----------
		clubs : list
			A list of Club Objects
		players : list
			A list of Player Objects

		Returns
		------- 
			A list of Club Objects 
		"""

		for club in clubs:
			for player in players:
				if player.club_id == club.id: 
					club.add_to_squad(player)
		return clubs 
	
	@staticmethod
	def define_formation(clubs: list) -> None:
		"""Modify the Club.start_eleven & Club.bench 
		
		Parameters
		----------
		clubs : list
			A list of Clubs Objects That have players in Club.squad

		Returns
		-------
			None
		"""
		
		for club in clubs:
			club.start_eleven = formation.starting_eleven(club.squad)
			club.bench = formation.backups(club.squad, club.start_eleven)
	
		return None 
	
	@staticmethod
	def define_schedule(clubs: list) -> list[list]:
		"""Generates a list of confronts between two different clubs.
		Each list has 2 elements a home and away team, two confronts can be
		equal if their positioning in the list is inverted
		ex: [team_a, team_b] , [team_b, team_a]

		Parameters
		----------
		clubs : list 
			A list of Club Objects

		Returns
		-------
			A list of lists containing two clubs in each one
		"""

		games = []
		for home in clubs:
			for away in clubs:
				if home != away : games.append([home, away]) 
		return games

	@staticmethod
	def prepare_games(games: list, stadiums: list, competition: str, competition_id: int, season: int) -> list[Game]:
		"""Transform data into Game Objects
		
		Parameters
		----------
		games : list
			A list of game data containing two clubs
		stadiums : list
			A list of Stadiums Objects
		competition : str
			Name of the competition of this games
		season : int
			Season relating to this games

		Returns
		-------
			A list of Game Objetcs 
		"""
		
		return [ Game(i[0], i[1], competition, competition_id, season, 1, choice(stadiums)) for i in games ]
	
	@staticmethod
	def prepare_cup_games(games: list, competition: str, competition_id: int, 
					   	  season: str, phase: str, game_number: int, stadiums: list, 
						  first_leg_home_goals: int=0, first_leg_away_goals: int=0) -> list[CupGame]:
		
		"""Transform data into CupGame objects

		Parameters
		---------
		games : list
			A list of game data containing two clubs
		competition : str
			Name of the competition of this games
		competition_id : int
			A int value for the competition id
		season : int
			Season relating to this games
		phase : str
			A string value containing the phase name ex: round of 32 | round of 16 | ...
		game_number : int
			A int value between 1 or 2 for the match number
		stadiums : list
			A list of Stadium Objects
		first_leg_home_goals : int
			A int value for the home first leg goals. Default value is 0
		first_leg_away_goals : int
			A int value for the away first leg goals. Default value is 0
		
		Returns
		-------
			A list of CupGame objects 
		"""
		
		return [ CupGame(i[0], i[1], competition, competition_id, season, phase, game_number, choice(stadiums), 
				   		 first_leg_home_goals=first_leg_home_goals, first_leg_away_goals=first_leg_away_goals ) for i in games 
		]

	@classmethod
	def prepare_clubs(cls, clubs_data: list, players_data: list) -> list[Club]:
		"""Prepare clubs & players by their respective data

		Parameters
		----------
		clubs_data : list
			A list containing clubs data
		players_data : list
			A list containing players data
		
		Returns 
		-------
			A list of club objects configure and prepared to player
		"""
		
		players = cls.players(players_data) # Instance player objects
		clubs = cls.clubs(clubs_data) # Instance club objects

		clubs = cls.add_players_to_clubs(clubs, players) # Add players to clubs
		cls.define_formation(clubs) # Define clubs formation

		return clubs


class CupHelper:
	"""
	Class focused on dealing with cup only functions

	Methods
	-------
	sort_simple_cup_confronts(clubs_id: list)
		Sort clubs confronts to the Copa Do Brasil
	invert_confronts(confronts: list)
		Preapre confronts for the second leg match
	run_cup_phase(phase: str, match_number: int, competition_id: int, games: list)
		Runs a cup phase
	"""
	
	@staticmethod
	def invert_confronts(confronts: list, competition: str, competition_id: int, season: str, phase: str,
					     game_number: int, stadiums: list) -> list[CupGame]:
		"""Prepare games 2 of 2

		Parameters
		----------
		confronts : list
			A list of game objects that alredy has been started
		competition : str
			Name of the competition of this games
		competition_id : int
			A int value for the competition id
		season : int
			Season relating to this games
		phase : str
			A string value containing the phase name ex: round of 32 | round of 16 | ...
		game_number : int
			A int value between 1 or 2 for the match number
		stadiums : list
			A list of Stadium Objects
		
		Returns
		-------
			A list of new CupGame updated with info necessary for the game 2 of 2
		"""

		games = []

		for conf in confronts:
			home = conf['clubs']['away']
			away = conf['clubs']['home']
			first_leg_home_goals = conf['cup_info']['first_leg_away_goals']
			first_leg_away_goals = conf['cup_info']['first_leg_home_goals']
			
			stadium = choice(stadiums)

			games.append(CupGame(home, away, competition, competition_id, season, 
								phase, game_number, stadium, 
								first_leg_home_goals=first_leg_home_goals, 
								first_leg_away_goals=first_leg_away_goals))

		return games
	
	@staticmethod
	def sort_simple_cup_confronts(clubs: list) -> list[list]:
		"""Groups the list into a two dimensional array with doubles random values 

		Parameters
		----------
		clubs : list
			A list containing a pair of Club objects

		Returns
		-------
			A list of lists with two Club objects inside of each one
		"""

		shuffle(clubs)

		data = []

		for _ in range(len(clubs) // 2):
			home = clubs.pop()
			away = clubs.pop()

			data.append([home, away])

		return data
	
	@staticmethod
	def run_cup_phase(phase: str, match_number: int, games: list, single_phase : int=0) -> list[CupGame]:
		"""Run games from a cup phase

		Parameters
		----------
		phase : str
			A string with cup phase
		match_number : int
			A int value between 1 and two if the game is home/away
		games : list
			A list of cup games 
		single_phase : int
			A int value for single_phase. 0 if False 1 if True
			
		Returns
		-------
			A list of CupGame that already been started
		"""
		
		logs = []

		for game in games:
			game.start()

			game_stats = logs_handler.get_game_stats(game.logs, game.home, game.away)
			stats_data = logs_handler.prepare_game_stats_logs_to_db(game_stats)

			# Get game stats
			home = games_controller.insert_game_stat_with_id_return(stats_data[0])
			away = games_controller.insert_game_stat_with_id_return(stats_data[1])

			# Game stats id's
			game_stats_ids = [ home[0][0], away[0][0] ]

			game_data = logs_handler.prepare_game_logs_to_db(game.logs, game_stats_ids)
			
			# insert game data and return id
			game_id = games_controller.insert_game(game_data)
			game_id = game_id[0][0]

			# insert penalty into database
			penalty_id = games_controller.insert_penalty(game.prepare_penalties_data())
			penalty_id = penalty_id[0][0]

			# prepare knock out data 
			knock_data = logs_handler.prepare_knock_out_logs_to_db(phase, single_phase, match_number, game_id, penalties_id=penalty_id)
			
			# insert knock out
			games_controller.insert_knock_out(knock_data)

			logs.append(game.logs)
			
		return logs