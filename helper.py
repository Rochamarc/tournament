from classes.player import Player
from classes.club import Club

class ClassConstructor:
	@staticmethod
	def reconstruct_players(players_data: list) -> list[Player]:	
		players = []

		for pd in players_data:
			players.append(Player(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5], pd[6], pd[7], pd[8]))

		return players

	@staticmethod
	def reconstruct_clubs(clubs_data: list) -> list[Club]:
		clubs = []
		for cd in clubs_data:
			clubs.append(Club(cd[0], cd[1], cd[2], cd[3], cd[4], cd[5]))

		return clubs 