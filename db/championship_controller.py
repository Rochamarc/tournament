import mysql.connector
from db.base_controller import BaseController

class ChampionshipsController(BaseController):
    """
    Class that manage the tournament.championships table

    ...

    Methods
    -------

    select_championships_table_by_club(season: int, club_id: int)
        Select championships table by club
    
    """
    
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

