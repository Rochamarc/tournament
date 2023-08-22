from classes.player import Player

class ClassConstructor:
	@staticmethod
	def reconstruct_players(players_data: list) -> list[Player]:	
		players = []

		for pd in players_data:
			players.append(Player(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5], pd[6], pd[7], pd[8]))

		return players