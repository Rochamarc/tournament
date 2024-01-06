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
        
        return cls.insert_registers(cls.get_query('insert', 'insert_game'), games_data)
    
    @classmethod
    def insert_game(cls, game_data: list) -> list[set]:
        """Insert a game data into tournament.games return his id

        Parameters
        ----------
        game_data : list
            A list with game data [season, hour, climate, weather, stadium, audience, ticket_value ]
        
        Returns
        -------
            A list containing a set with his id
        """
        
        # insert a game into database
        cls.insert_register(cls.get_query('insert', 'insert_game'), game_data)

        return cls.select_register(cls.get_query('select','select_last_game'))


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

        cls.insert_register(cls.get_query('insert', 'insert_game_stats'), game_data)
        
        return cls.select_last_game_stats_id()
    
    @classmethod
    def select_last_game_stats_id(cls) -> list:
        """Select the last id from tournament.game_stats 
        
        Returns
        -------
            A list with id from last game_stats row
        """
        
        return cls.select_register(cls.get_query('select','select_game_stats_id_last_inserted'))

    @classmethod
    def insert_knock_out(cls, knock_out_data: list) -> None:
        """Insert a knock_out_data into tournament.knock_out

        Parameters
        ----------
        knock_out_data : list
            Data for knock out phase, single_match, match_number, game_id, penalty_id
            
        Returns
        -------
            None
        """
        cls.insert_register(cls.get_query('insert', 'insert_knock_out_first_leg'), knock_out_data)

        return None
    
    @classmethod
    def insert_penalty(cls, data: list) -> list[set]:
        """Insert a penalty data into tournament.penalties

        Parameters
        ----------
        data : list
            A list continaint 0 or 1 for penalty | a value for away_penalty | a int value for away penalty
        
        Returns
        -------
            A int for penalty id
        """

        cls.insert_register(cls.get_query('insert', 'insert_penalty'), data)

        return cls.select_register(cls.get_query('select', 'select_last_penalty'))