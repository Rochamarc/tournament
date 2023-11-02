import mysql.connector
from db.base_controller import BaseController

class StadiumsController(BaseController):
    """
    Class that manage the tournament.stadiums

    ...

    Methods
    -------

    select_all_stadiums()
        Select all stadiums from database
    """
        
    @classmethod
    def select_all_stadiums(cls) -> list[set]:
        """Select all stadiums from database
        
        Returns
        -------
            A list of lists with stadium data
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_stadiums'))

        stadiums = cursor.fetchall()

        conn.close()
        return stadiums 