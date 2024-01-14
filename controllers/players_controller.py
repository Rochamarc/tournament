from controllers.base_controller import BaseController

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

        return cls.insert_registers(cls.get_query('insert', 'insert_market_value'), market_value_datas)

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

    @classmethod
    def insert_player_contracts(cls, player_contracts_data: list) -> None:
        """Insert a list of player_contracts_data into tournament.player_contracts

        Parameters
        ----------
        player_contracts_data : list
            A list of lists containing: 
            start: str, end: str, salary: int, club_id: int, player_id: int
        
        Returns
        -------
            None
        """
        
        return cls.insert_registers(cls.get_query('insert', 'insert_player_contracts'), player_contracts_data)

    @classmethod
    def select_players_with_no_contract(cls) -> list[set]:
        """Select a list of Free Agent players data from tournament.player_contracts

        Returns
        -------
            A list of sets with [player_contracts.id, players.id]
        """

        return cls.select_register(cls.get_query('select','select_players_with_no_contract'))

    @classmethod
    def select_players_with_end_contract(cls, season: str) -> list[set]:
        """Select a list of Free Agent players data from tournament.player_contracts

        Parameters
        ----------
        season : str
            An string value with end of season 
        
        Returns
        -------
            A list of sets with [player_contracts.id, players.id]
        """

        return cls.select_register(cls.get_query('select', 'select_players_with_end_contract'), season)
    @classmethod
    def insert_skills(cls, skills_data: list, season: str) -> None:
        """Insert a list of overall data into tournament.overall
        
        Parameters
        ----------
        overall_data : list
            A list of list containing
            positioning: int, reflexes: int, diving: int, standing_tackle: int, physical: int, 
            passing: int, dribbling: int, long_shot: int, finishing: int, player_id: int
        
        Returns
        -------
            None
        """

        for skill in skills_data:   
            skill.insert(0, season) # insert season at data

            if len(skill) == 5:
                query = cls.get_query('insert', 'insert_gk_skills')
            else:
                query = cls.get_query('insert', 'insert_skills')
            
            cls.insert_register(query, skill)
        
    @classmethod
    def select_skills(cls, season: str) -> list[set]:
        """Select a list of skills_data

        Parameters
        ----------
        season : str
            A string value with valid season 
        
        Returns
        -------
            A list of sets with all skills data. last arg is player_id
        """

        return cls.select_register(cls.get_query('select', 'select_skills_by_season'), [season])
    
    @classmethod
    def select_last_skills(cls, season: str) -> list[set]:
        """Select the last skills inserted from tournament.skills

        Returns
        -------
            A list with 30 length containing [
            positioning,
            reflexes,
            diving,
            standing_tackle,
            physical,
            passing,
            dribbling,
            long_shot,
            finishing,
            player_id
            ]
        """

        return cls.select_register(cls.get_query('select', 'select_last_skills'), [season])