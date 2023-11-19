from db.base_controller import BaseController
import mysql.connector 

class GamesController(BaseController):
    """
    Class that manage the tournament.games, game_stats & knock_out table

    ...

    Methods
    -------

    insert_games_list(games_data: list)
        Insert a list of tournament.games in database
    insert_game_stat_with_id_return(game_data)
        Insert a tournament.game_stats in database
    select_last_id()
        Select the last tournament.game_stats inserted 
    insert_knock_out(knock_out_data: list) 
        Insert a tournament.knock_out in database 
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
    def insert_game(cls, game_data: list) -> list[str]:
        """Insert a game data into tournament.games without tournament.games_stats foreign key and return his id

        Parameters
        ----------
        game_data : list
            A list with game data [season, hour, climate, weather, stadium, audience, ticket_value ]
        
        Returns
        -------
            A list containing a set with his id
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_insert_query(''))
        pass



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

    @classmethod
    def insert_knock_out(cls, knock_out_data: list) -> None:
        """Insert a knock_out_data into tournament.knock_out

        Parameters
        ----------
        knock_out_data : list
            A list containing data to knock_out table 
            [ season, phase, single_match, match_number, home_id, away_id, home_game_stats, away_game_stats, competition_id ]
        
        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_insert_query('insert_knock_out'), knock_out_data)
        
        conn.commit()
        conn.close()

        return None