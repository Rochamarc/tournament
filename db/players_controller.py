from db.base_controller import BaseController

class PlayersController(BaseController):
    """
    Class that manage the tournament.players

    ...

    Methods
    -------
    insert_players(players_data: list)
        Insert a list of tournament.players in database
    select_last_players()
        Select the 30 last tournament.players inserted
    select_all_players_id()
        Select all the player's id of tournament.players
    select_all_players_id_position()
        Select all the player's id and position of tournament.players
    select_players_by_club(club_name: str, season: str)
        Select all players with contract with a specific club
    select_players_with_contract(season: str)
        Select all players with contract with a club
    delete_players()
        Delete all players from database
    insert_player_stats(stats_data : list)
        Insert a tournament.stats in database
    insert_player_stats(stats_datas : list)
        Insert a list of tournament.stats in database
    """
        
    @classmethod
    def insert_players(cls, players_data: list) -> None:
        """Insert a list of players_data into tournament.players

        Parameters
        ----------
        players_data : list
            A list of lists containing: name: str, nationality: str, position: str, birth: int, height: float, weight: float, foot: str
        
        Returns
        -------
            None
        """
        
        return cls.insert_registers(cls.get_query('insert', 'insert_players'), players_data)

    @classmethod
    def insert_player_stats(cls, stats_data : list) -> None:
        """Insert stats_data into tournament.stats

        Parameters
        ----------
        stats_data : list
            A list containing [ season: str, matches: int, goals: int, assists: int, tackles: int, passes: int, 
            wrong_passes: int, intercepted_passes: int, clearences: int, stolen_balls: int, clean_sheets: int,
            defenses: int, difficult_defenses: int, goals_conceded: int, player_id: int, game_id: int ]
        
        Returns
        -------
            None
        """

        return cls.insert_register(cls.get_query('insert', 'insert_stats'), stats_data)
    
    @classmethod
    def insert_players_stats(cls, stats_datas : list) -> None:
        """Insert a list of stats_data into tournament.stats

        Parameters
        ----------
        stats_datas : list
            A list of data list containing [ season: str, matches: int, goals: int, assists: int, tackles: int, passes: int, 
            wrong_passes: int, intercepted_passes: int, clearences: int, stolen_balls: int, clean_sheets: int,
            defenses: int, difficult_defenses: int, goals_conceded: int, player_id: int, game_id: int ]
        
        Returns
        -------
            None
        """

        return cls.insert_registers(cls.get_query('insert', 'insert_stats'), stats_datas)
    
    @classmethod
    def insert_players_market_value(cls, market_value_datas: list) -> None:
        """Insert a list of market_value data into tournament.market_value

        Parameters
        ----------
        market_value_datas : list
            A list of data containing [
                season,
                value,
                player_id
            ]
        
        Returns
        -------
            None
        """

        return cls.insert_registers(cls.get_query('insert', 'insert_market_value'))

    @classmethod
    def select_last_players(cls) -> list:
        """Select the last players from tournament.players

        Returns
        -------
            A list with 30 length containing player's id, birth & position
        """

        return cls.select_register(cls.get_query('select','select_last_players'))
        
    @classmethod
    def select_all_players_id(cls) -> list:
        """Select the player's id from tournament.players

        Returns
        -------
            A list of sets with (id,) column from the tournament.players
        """
        
        return cls.select_register(cls.get_query('select','select_id_from_players'))

    @classmethod
    def select_all_players_id_position(cls) -> list[set]:
        """Select the player's id and position from tournament.players 

        Returns
        -------
            A list of sets with (id, position,) from tournament.players
        """

        return cls.select_register(cls.get_query('select','select_id_position_from_players'))


    @classmethod
    def select_players_by_club(cls, club_name: str, season: str) -> list[set]:
        """Select players with contract of a club, this aggregates players table
        with player_contracts, clubs & skills

        Parameters
        ----------
        
        club_name : str
            Club's name that will be used as condition to clubs.name
        season : str
            Season that will be used as parameter to player_contracts & skills

        Returns
        -------
            A list of Players data 
        """

        return cls.select_register(cls.get_query('select','select_players_by_clubs'), [club_name, season])


    @classmethod
    def select_players_with_contract(cls, season: str) -> list[set]:
        """Select all players that have a contract with a club, this aggregates players table
        with player_contracts, clubs & skills

        Parameters
        ----------

        season : str
            Season that will be used as parameter to player_contracts & skills

        Returns
        -------
            A list of Players data 
        """        

        return cls.select_register(cls.get_query('select','select_players_by_contracts'), [season])
    
    @classmethod
    def select_players_by_contracts_and_class(cls) -> list[set]:
        """Select players by contracts

        Returns
        -------
            A list of sets with ['player_id', 'club_class', 'position']
        """
        
        return cls.select_register(cls.get_query('select','select_players_and_clubs_class_by_contracts'))
    
    @classmethod
    def delete_players(cls) -> None:
        """Delete all players and his constraints

        Returns
        -------
            None
        """

        return cls.delete_register(cls.get_delete_query('delete_players'))

if __name__ == "__main__":
    print(PlayersController().select_players_by_club('2022'))
