import mysql.connector
from base_controller import BaseController

class PlayersController(BaseController):	
	@classmethod
	def get_by_contract(cls):
		''' Return all players with contract '''
		conn = mysql.connector.connect(**cls.database_config)
		cursor = conn.cursor()

		cursor.execute(cls.get_query('select_players_by_contract'))
		players = cursor.fetchall()

		conn.close()
		return players

	@classmethod
	def get_all(cls):
		''' Return all players data'''  
		conn = mysql.connector.connect(**cls.database_config)
		cursor = conn.cursor()

		cursor.execute(cls.get_query('select_players'))
		players = cursor.fetchall()

		conn.close()
		return players	

	@classmethod
	def get_by_club(cls, club: str) -> list:
		''' Return players by club '''

		conn = mysql.connector.connect(**cls.database_config)
		cursor = conn.cursor()

		cursor.execute(cls.get_query('select_players_by_club'), [club])
		players = cursor.fetchall()

		conn.close()
		return players


if __name__ == "__main__":
    print(PlayersController().get_by_club('Fluminense'))
