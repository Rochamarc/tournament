import mysql.connector
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
    """
    
    @classmethod
    def insert_championship(cls, clubs_data: list) -> None:
        """Insert the championships table with all stats with 0

        Parameters
        ----------
        clubs_data : list
            Each list has to have [ season, club_id, division_id ]
        
        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()
        
        for club_data in clubs_data:
            cursor.execute(cls.get_insert_query('insert_championships'), club_data)
        
        conn.commit()
        conn.close()

        return None
    
    @classmethod
    def select_championships_to_insert(cls, division_name: str) -> list[set]:
        """Select championships table ordered by points

        Parameters
        ----------
        division_name : str
            Name of division that will be used as where clause
        
        Returns
        -------
            A list of sets with [ club_id, division_id ]
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_championships_to_insert'), [division_name])
        values = cursor.fetchall()

        conn.close()
        return values

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

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_championship_by_club'), [season, club_id])
        values = cursor.fetchall()

        conn.close()
        return values
    
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
                
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_all_table_by_division'), [season, division_name])
        values = cursor.fetchall()

        conn.close()
        return values

    @classmethod
    def update_championship_table(cls, data: list) -> None:
        """Update the club's championships table based on division
        
        Parameters
        ----------
        data : list
            A list containing: points, win, loss, draw, goals_for, goals_away, goal_diff, club_id, season
        
        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_update_query('update_championship'), data)
        
        conn.commit()
        conn.close()

        return None

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
            A list with a set with [ name, matches, win, draw, loss, goals_for, goals_away, goals_diff, points ]
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_champion'), [season, division_name])

        club = cursor.fetchall()
        conn.close()

        return club

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

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_relegated_zone'), [season, division_name])

        clubs = cursor.fetchall()
        conn.close()

        return clubs 
     
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

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_promoted_zone'), [season, division_name])

        clubs = cursor.fetchall()
        conn.close()

        return clubs 