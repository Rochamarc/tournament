from db.base_controller import BaseController
import mysql.connector 

class GamesController(BaseController):
    """
    Class that manage the tournament.games & game_stats table

    ...

    Methods
    -------

    insert_games_list(games_data: list)
        Insert a list of tournament.game in database
    insert_game_stat_with_id_return(game_data)
        Insert a tournament.game_stats in database
    select_last_id()
        Select the last tournament.game_stats inserted 
    """
        
    @classmethod
    def insert_games_list(cls, games_data: list) -> None:
        """Insert a list of games_data into tournament.games 

        Parameters
        ----------

        games_data : list
            A list of lists with games_data
        
        Returns
        -------
            None
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for game_data in games_data:
            cursor.execute(cls.get_insert_query('insert_game'), game_data)

        conn.commit()
        conn.close()

    @classmethod
    def insert_game_stat_with_id_return(cls, game_data: list) -> list:
        """Insert a list of games_data into tournament.game_stats 

        Parameters
        ----------

        games_data : list
            A list with game_stats data
        
        Returns
        -------
            A list containing the game_stats.id from the game_stats inserted in db
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_insert_query('insert_game_stats'), game_data)
        conn.commit()

        conn.close()
        return cls.select_last_id()
    
    @classmethod
    def select_last_id(cls) -> list:
        """Select the last id from tournament.game_stats 
        
        Returns
        -------
            A list with id from last game_stats row
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_game_stats_id_last_inserted'))
        id = cursor.fetchall()
        
        conn.close()
        return id 