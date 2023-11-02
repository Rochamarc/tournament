import mysql.connector
from db.base_controller import BaseController

class OverallController(BaseController):
    """
    Class that manage the tournament.overall

    ...

    Methods
    -------
    insert_overall(overall_data: list)
        Insert a list of tournament.overall in database
    """

    @classmethod
    def insert_overall(cls, overall_data: list) -> None:
        """Insert a list of overall data into tournament.overall
        
        Parameters
        ----------
        overall_data : list
            A list of list containing
            season: str, overall: int, player_id: int
        
        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()
        
        for overall in overall_data:
            cursor.execute(cls.get_insert_query('insert_overall'), overall)
        
        conn.commit()
        conn.close()

        return None