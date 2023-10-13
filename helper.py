from classes.club import Club
from classes.formation import Formation
from classes.player import Player
from classes.stadium import Stadium

from game import Game 

from random import choice 

formation = Formation()

class ClassConstructor:
	@staticmethod
	def players(players_data: list) -> list[Player]:	
		''' Receive a players data list by the the following pattern =>
		[ id, name, nationality, birth, position, height, weight, foot, overall, club_id ] 
		return a list of Player objetcts
		'''
		return [ Player(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5], pd[6], pd[7], pd[8], pd[9]) for pd in players_data ]

	@staticmethod
	def clubs(clubs_data: list) -> list[Club]:
		''' Receive a clubs data list by the following pattern => 
		[ club_id, club_name, club_country ] 
		return a list of Club objects
		'''

		return [ Club(cd[0], cd[1], cd[2]) for cd in clubs_data ]
	
	@staticmethod
	def stadiums(stadiums_data: list) -> list[Stadium]:
		''' Receive a stadium data list by the following pattern => 
		[ stadium_name, stadium_location, stadium.capacity ] 
		return a list of Stadium objects
		'''
		return [ Stadium(sd[0], sd[1], sd[2]) for sd in stadiums_data ] 
	

	@staticmethod
	def add_players_to_clubs(clubs: list, players: list) -> list[clubs]:
		''' Add players to squad and return the list of clubs '''

		for club in clubs:
			for player in players:
				if player.club_id == club.id: 
					club.add_to_squad(player)
		return clubs 
	
	@staticmethod
	def define_formation(clubs: list) -> None:
		''' Return None, just change the players situation inside the Club objects '''
		
		for club in clubs:
			club.start_eleven = formation.starting_eleven(club.squad)
			club.bench = formation.backups(club.squad, club.start_eleven)
	
		return None 
	
	@staticmethod
	def define_schedule(clubs_list: list):
		''' Return a list of lists wich one with home_team and away_team '''

		games = []
		for home in clubs_list:
			for away in clubs_list:
				if home != away : games.append([home, away]) 
		return games

	@staticmethod
	def prepare_games(games: list, stadiums: list, competition: str, season: int) -> list[Game]:
		''' Return a list of Game objetcs '''
		return [ Game(i[0], i[1], competition, 1, season, choice(stadiums)) for i in games ]