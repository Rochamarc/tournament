import mysql.connector

database_config = {
    'user': 'tournament_user',
    'password': 'tournament_pass',
    'database': 'tournament_name',
    'host': 'localhost'
}

class NamesController:
    """
    Class that handle tournament_name database

    Methods
    -------
    insert_first_names(first_names: list, nationality: str)
        Insert first names in database
    insert_last_names(last_names: list, nationality: str)
        Insert last names in database
    """
    
    @staticmethod
    def insert_first_names(first_names: list, nationality: str) -> None:
        """Insert names into the tournament_name.first_names 
        
        Parameters
        ----------
        first_names : list
            A list of first names
        nationality : str
            A string with the nationality of the names
        
        Returns
        -------
            None
        """
        
        conn = mysql.connector.connect(**database_config)
        cursor = conn.cursor()

        for first_name in first_names:
            cursor.execute('INSERT INTO first_names VALUES(NULL, %s, %s);', [first_name, nationality])
        
        conn.commit()
        conn.close()

        return None

    @staticmethod
    def insert_last_names(last_names: list, nationality: str) -> None:
        """Insert names into the tournament_name.last_names 
        
        Parameters
        ----------
        last_names : list
            A list of last names
        nationality : str
            A string with the nationality of the names
        
        Returns
        -------
            None
        """        

        conn = mysql.connector.connect(**database_config)
        cursor = conn.cursor()

        for last_name in last_names:
            cursor.execute('INSERT INTO last_names VALUES(NULL, %s, %s);', [last_name, nationality])
        
        conn.commit()
        conn.close()

        return None 