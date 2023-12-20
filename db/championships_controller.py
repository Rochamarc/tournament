from db.base_controller import BaseController

class ChampionshipsController(BaseController):
    """
    Class that manage the tournament.championships table

    ...

    Methods
    -------

    insert_championships(clubs_data: list)
        Insert default championships table
    select_championships_to_insert(divison_name: str)
        Select championships table ordered by points
    select_championships_table_by_club(season: int, club_id: int)
        Select one championships row by club
    select_championship_table_by_division(season: int, division_name: str)
        Select all divisions championships rows by division & season
    update_championship_table(data: list)
        Update a championships row
    select_champion(season: str, division_name: str)
        Select championship champion by season & division
    select_relegated(season: str, division_name: str)
        Select championship relegated clubs by season & division
    select_promoted(season: str, division_name: str)
        Select championship promoted clubs by season & division
    select_serie_a_cup(season: str)
        Select serie a clubs id by season
    select_serie_b_c_cup(season: str)
        Select serie b & serie c clubs id by season
    """
    
    @classmethod
    def insert_championship(cls, clubs_data: list) -> None:
        """Insert the championships table with all stats with 0

        Parameters
        ----------
        clubs_data : list
            Each list has to have [ season, club_id, division_id ]
        competition_name : str
            A string containing competition's name

        Raises
        ------
            Exception if one club_id has a table associate with the season

        Returns
        -------
            None
        """
        
        for club in clubs_data:
            club_id = club[1]
            season = club[0]

            if cls.check_for_initial_table(club_id, season):
                raise Exception("Club with id: {}, is already associate to a table with season {}".format(club_id, season))

        return cls.insert_registers(cls.get_insert_query('insert_championships'), clubs_data)

    
    @classmethod
    def select_championships_to_insert(cls, division_name: str, previous_season: int) -> list[set]:
        """Select championships table ordered by points

        Parameters
        ----------
        division_name : str
            Name of division that will be used as where clause
        previous_season : int
            A int value for the previous tables

        Returns
        -------
            A list of sets with [ club_id, division_id ]
        """
        return cls.select_register(cls.get_select_query('select_championships_to_insert'), data=[division_name, previous_season])


    @classmethod
    def select_championship_table_by_club(cls, season: int, club_id: int) -> list[set]:
        """Select the club's championships table by his id

        Parameters
        ----------
        season : int
            To select the season of the championships
        club_id : int
            To select the id from the club's championships

        Returns
        -------
            A list containing 
            matches, win, draw, loss, goals_for, goals_away, goals_conceded, goals_diff, points
        """

        return cls.select_register(cls.get_select_query('select_championship_by_club'), [season, club_id])
        
    @classmethod
    def select_championship_table_by_division(cls, season: int, division_name: str) -> list[set]:
        """Select all the rows of the championsips table based on the season and divison

        Parameters
        ----------
        season : int
            To select the season of the championships
        division_name : str
            To select the championships division
        
        Returns
        -------
            A list of lists containing 
            matches, win, draw, loss, goals_for, goals_away, goals_diff, points
        """

        return cls.select_register(cls.get_select_query('select_championship_by_division'), [season, division_name])

    @classmethod
    def update_championship_table(cls, data: list, competition_name: str) -> None:
        """Update the club's championships table based on division
        
        Parameters
        ----------
        data : list
            A list containing: points, win, loss, draw, goals_for, goals_away, club_id, season
        competition_name : str
            A string containing competition's name
            
        Raises
        ------
            Exception if club has more than 38 matches in table 
            
        Returns
        -------
            None
        """

        club_id = data[-2]
        season = data[-1]
   
        if not cls.check_for_38_matches(club_id, season, competition_name):
            raise Exception("Club with id: {}, already has 38 matches in {} season {}".format(club_id, competition_name, season))
   
        return cls.update_register(cls.get_update_query('update_championship'), data)
    
    @classmethod
    def select_champion(cls, season: str, division_name: str) -> list[set]:
        """Select the first row from championsips 

        Parameters
        ----------
        season : str
            A string containing the season of championship
        division_name : str
            A string containing the name of the division

        Returns
        -------
            A list with a set with [ season, division_id, club_id ]
        """

        return cls.select_register(cls.get_select_query('select_champion'), [season, division_name])
        
    @classmethod
    def select_relegated(cls, season: str, division_name: str) -> list[set]:
        """Select the 4 last rows from championsips 

        Parameters
        ----------
        season : str
            A string containing the season of championship
        division_name : str
            A string containing the name of the division

        Returns
        -------
            A list with a set with [ name, matches, win, draw, loss, goals_for, goals_away, goals_diff, points ]
        """

        return cls.select_register(cls.get_select_query('select_relegated_zone'), [season, division_name])

     
    @classmethod
    def select_promoted(cls, season: str, division_name: str) -> list[set]:
        """Select the first 4 rows from championsips 

        Parameters
        ----------
        season : str
            A string containing the season of championship
        division_name : str
            A string containing the name of the division

        Returns
        -------
            A list with a set with [ name, matches, win, draw, loss, goals_for, goals_away, goals_diff, points ]
        """

        return cls.select_register(cls.get_select_query('select_promoted_zone'), [season, division_name])
    
    @classmethod
    def select_serie_a_cup(cls, season: str) -> list[set]:
        """Select club's id from serie a championships by season

        Parameters
        ----------
        season : str
            A string containing the season of championship

        Returns
        -------
            A 20 length list with a set of id's
        """
        
        return cls.select_register(cls.get_select_query('select_id_from_championships_serie_a'), [season])
    
    @classmethod
    def select_serie_b_c_cup(cls, season: str) -> list[set]:
        """Select 12 random club's id from serie b and c championships by season

        Parameters
        ----------
        season : str
            A string containing the season of championship

        Returns
        -------
            A 12 length list with a set of id's
        """

        return cls.select_register(cls.get_select_query('select_id_from_championships_serie_b_c'), [season])

    @classmethod
    def check_for_38_matches(cls, club_id: int, season: str, competition_name) -> bool:
        """Check if the table already has 38 matches for the club 
        
        Parameters
        ----------
            club_id : int

            season : str

            competition_name : str

        Returns
        -------
            True if returns some data False if returns noting 
        """

        data = cls.check_register(cls.get_check_query('check_championships'), [club_id, season, competition_name])

        if data:
            return True
        return False

    @classmethod
    def check_for_initial_table(cls, club_id: int, season: str) -> bool:
        """Check if the club has another table insertion with specific season

        Parameters
        ----------
        club_id : int
            A int value that refere to club's id
        season : str
            A string value containing season
        
        Returns
        -------
            A True if has data and false if returns nothing
        """

        data = cls.check_register(cls.get_check_query('check_championships_intial_table'), [club_id, season])

        if data:
            return True 
        return False