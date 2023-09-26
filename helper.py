from classes.player import Player
from classes.club import Club

class ClassConstructor:
	@staticmethod
	def players(players_data: list) -> list[Player]:	
		players = []

		for pd in players_data:
			players.append(Player(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5], pd[6], pd[7], pd[8], pd[9]))

		return players

	@staticmethod
	def clubs(clubs_data: list) -> list[Club]:
		clubs = []
		for cd in clubs_data:
			clubs.append(Club(cd[0], cd[1], cd[2]))

		return clubs 

	@staticmethod
	def add_players_to_clubs(clubs: list, players: list) -> list[clubs]:
		''' Add players to squad and return the list of clubs '''

		for club in clubs:
			for player in players:
				if player.club_id == club.id: 
					club.add_to_squad(player)
					players.remove(player)
		return clubs 