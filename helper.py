from classes.club import Club
from classes.formation import Formation
from classes.player import Player
from classes.stadium import Stadium

from game import Game 

from random import choice 

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
	def prepare_games(games: list, stadiums: list, competition: str, season: int) -> list[Game]:
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
		
		return [ Game(i[0], i[1], competition, season, 1, choice(stadiums)) for i in games ]