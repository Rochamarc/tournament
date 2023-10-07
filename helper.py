from classes.player import Player
from classes.club import Club

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
	def add_players_to_clubs(clubs: list, players: list) -> list[clubs]:
		''' Add players to squad and return the list of clubs '''

		for club in clubs:
			for player in players:
				if player.club_id == club.id: 
					club.add_to_squad(player)
		return clubs 