import mysql.connector
from db.base_controller import BaseController

class CoachesController(BaseController):
    """
    Class that manage the tournament.coaches

    ...

    Methods
    -------
    insert_coaches(coaches_data: list)
        Insert a list of tournament.coaches in database
    select_id()
        Select all coach's id
    """

    @classmethod
    def insert_coaches(cls, coaches_data: list) -> None:
        """Insert a list of coaches_data into tournament.coaches

        Parameters
        ----------
        coaches_data : list
            A list of lists containing: 
            name: str, nationality: str, birth: int
        
        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for coach_data in coaches_data:
            cursor.execute(cls.get_insert_query('insert_coaches'), coach_data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def select_id(cls) -> list[set]:
        """Select id from coaches

        Returns
        -------
            A list of lists with: id
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_id_from_coaches')) 
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def delete_coaches(cls) -> None:
        """Delete all coaches and his constraints

        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_delete_query('delete_coaches'))

        conn.close()

        return None 

        

if __name__ == "__main__":
    print(CoachesController().select_id())