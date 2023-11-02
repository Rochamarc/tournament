import mysql.connector
from db.base_controller import BaseController

class ClubsController(BaseController):
    """
    Class that manage the tournament.clubs table

    ...

    Methods
    -------
    select_id_name()
        Select all club's id and name
    select_id()
        Select all club's id
    select_serie_a_clubs()
        Select all clubs by serie a
    select_serie_b_clubs()
        Select all clubs by serie b
    select_serie_c_clubs()
        Select all clubs by serie c
    """
    
    @classmethod
    def select_id_name(cls) -> list[set]:
        """Select id and name from clubs

        Returns
        -------
            A list of lists with: id, name
        """

        conn = mysql.connector.connect(cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_id_name_from_clubs'))
        res = cursor.fetchall()

        conn.close()

        return res
    
    @classmethod
    def select_id(cls) -> list[set]:
        """Select id from clubs

        Returns
        -------
            A list of lists with: id
        """

        res = cls.select_id_name()
        
        return [ r[0] for r in res ]

    @classmethod
    def select_serie_a_clubs(cls) -> list[set]:
        """Select all clubs that belongs to Serie A division

        Returns
        -------
            A list of lists with: id, name, country, division 
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_serie_a_clubs'))
        clubs = cursor.fetchall()

        conn.close()
        return clubs 

    @classmethod
    def select_serie_b_clubs(cls) -> list[set]:
        """Select all clubs that belongs to Serie B division

        Returns
        -------
            A list of lists with: id, name, country, division 
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_serie_b_clubs'))
        clubs = cursor.fetchall()

        conn.close()
        return clubs 
    

    @classmethod
    def select_serie_c_clubs(cls) -> list[set]:
        """Select all clubs that belongs to Serie C division

        Returns
        -------
            A list of lists with: id, name, country, division 
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_serie_c_clubs'))
        clubs = cursor.fetchall()

        conn.close()
        return clubs 
    
if __name__ == "__main__":
    print(ClubsController().select_serie_a_clubs())