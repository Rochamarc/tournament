import mysql.connector

select_players = """
SELECT players.id, players.name, players.nationality, players.birth_year, players.position, 
players.height, players.weight, players.foot, players_overall.overall
FROM players
INNER JOIN players_overall
	ON players.id = players_overall.id_player;
"""
select_players_by_contract = """
SELECT players.id, players.name, players.nationality, players.birth_year, players.position, 
players.height, players.weight, players.foot, players_overall.overall, clubs.name
FROM players, clubs
INNER JOIN players_overall 
INNER JOIN players_contract
	ON players.id = players_overall.id_player 
 	AND players.id = players_contract.id_player 
	AND clubs.id = players_contract.id_club;
"""


database_config = {
    'user': 'tournament_user',
    'host': 'localhost',
    'password': 'tournament_pass',
    'database': 'football'
}


class PlayersController():	
	@staticmethod
	def get_players_with_contract():
		''' Return all players with contract data'''
		conn = mysql.connector.connect(**database_config)
		cursor = conn.cursor()

		cursor.execute(select_players)
		players = cursor.fetchall()

		return players

	@staticmethod
	def get_all_players():
		''' Return all players data'''
		conn = mysql.connector.connect(**database_config)
		cursor = conn.cursor()

		cursor.execute(select_players)
		players = cursor.fetchall()

		return players	

if __name__ == "__main__":
    print(PlayersController.get_players_with_contract())
