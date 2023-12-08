from classes.club import Club
from classes.formation import Formation
from classes.player import Player
from classes.stadium import Stadium

from db.games_controller import GamesController

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

    ...

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

		return [ Player(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5], pd[6], pd[7], pd[8], pd[9], pd[10], pd[11], pd[12], pd[13], pd[14], pd[15], pd[16], pd[17]) for pd in players_data ]

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

		return [ Club(cd[0], cd[1], cd[2]) for cd in clubs_data ]
	
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

		return [ Stadium(sd[0], sd[1], sd[2], sd[3]) for sd in stadiums_data ] 
	

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
						  first_leg_home_goals: int=0, first_leg_away_goals: int=0) -> list[Game]:
		"""
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

	sort_simple_cup_confronts(clubs_id: list)
		Sort clubs confronts to the Copa Do Brasil
	invert_confronts(confronts: list)
		Preapre confronts for the second leg match
	run_cup_phase(phase: str, match_number: int, competition_id: int, games: list)
		Runs a cup phase
	"""
	
	@staticmethod
	def invert_confronts(confronts: list) -> list:
		"""Prepare data for the 2 of 2 game

		Parameters
		----------
		confronts : list
			A list of lists containing a pair of Club Objects

		Returns
		-------
			A list of lists with inverted club position
		"""

		return [ [confront[-1], confront[0]] for confront in confronts ]
	
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

		for _ in range(len(clubs)//2):
			home = clubs.pop()
			away = clubs.pop()

			data.append([home, away])

		return data
	
	@staticmethod
	def run_cup_phase(phase: str, match_number: int, competition_id: int, games: list) -> list:
		"""Run all games from a cup

		Parameters
		----------
		phase : str
			A string with cup phase
		games : list
			A list of games 
		"""
		
		single_phase = False 

		for game in games:
			game.start()

			game_stats = logs_handler.get_game_stats(game.logs, game.home, game.away)
			stats_data = logs_handler.prepare_game_stats_logs_to_db(game_stats)

			# Get game stats
			home = games_controller.insert_game_stat_with_id_return(stats_data[0])
			away = games_controller.insert_game_stat_with_id_return(stats_data[1])

			# Game
			game_stats_ids = [home[0][0], away[0][0]]

			game_data = logs_handler.prepare_game_logs_to_db(game.logs, game_stats_ids)
			game_id = games_controller.insert_game(game_data)

			# knock out data
			# this is obsolete, the kncok_out table has changed
			knock_data = logs_handler.prepare_knock_out_logs_to_db(phase, single_phase, match_number, game_id[0][0])

			games_controller.insert_knock_out(knock_data)