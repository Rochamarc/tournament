from db.base_controller import BaseController

import mysql.connector

class ChampionsController(BaseController):
    """
    Class that manage the tournament.champíons table

    ...

    Methods
    -------

    insert_champion(season: str, division_id, club_id: int)
        Insert a league title to a club
    """

    @classmethod
    def insert_champion(cls, season: str, division_id: int, club_id: int) -> None:
        """Insert a league title to a club

        Parameters
        ----------
        season : str
            A string that refers to the season won by club
        division_id : int
            A int value that refers to division id
        club_id : int
            A int value that referes to club id

        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_insert_query('insert_champions'), [season, division_id, club_id])
        
        conn.commit()
        conn.close()

        return None