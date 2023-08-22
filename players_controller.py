import mysql.connector


database_config = {
    'user': 'tournament_user',
    'host': 'localhost',
    'password': 'tournament_pass',
    'database': 'football'
}


def get_query(file_name: str) -> str:
	''' Return a string query by a file in sql '''
	try:
		with open('{}.sql'.format(file_name), 'r') as file:
			return ''.join(file.readlines())
	except: 
		raise FileNotFoundError("File name doesn't exists")


class PlayersController():	
	@staticmethod
	def get_by_contract():
		''' Return all players with contract '''
		conn = mysql.connector.connect(**database_config)
		cursor = conn.cursor()

		cursor.execute(get_query('select_players_by_contract'))
		players = cursor.fetchall()

		return players

	@staticmethod
	def get_all():
		''' Return all players data'''  
		conn = mysql.connector.connect(**database_config)
		cursor = conn.cursor()

		cursor.execute(get_query('select_players'))
		players = cursor.fetchall()

		return players	

	@staticmethod
	def get_by_club(club: str) -> list:
		''' Return players by club '''

		conn = mysql.connector.connect(**database_config)
		cursor = conn.cursor()

		cursor.execute(get_query('select_players_by_club'), [club])
		players = cursor.fetchall()

		return players


if __name__ == "__main__":
    print(PlayersController().get_by_club('Fluminense'))
