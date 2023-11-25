import mysql.connector

class BaseController:
    """
    Base class that contains every property and functions used in other controllers
    """

    @classmethod
    def get_delete_query(cls, file_name: str) -> str:
        """Get one query on db/queries/select

        Parameters
        ----------
        file_name : str
            Name of the file inside the path without the file extension
        
        Returns
        -------
            A string with the query in the file

        Raises
        ------
        FileNotFoundError
            If the file doesnt exists
        """
        
        file_path = 'db/queries/delete/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File {} doesn't exists".format(file_path))


    @classmethod
    def get_select_query(cls, file_name: str) -> str:
        """Get one query on db/queries/select

        Parameters
        ----------
        file_name : str
            Name of the file inside the path without the file extension
        
        Returns
        -------
            A string with the query in the file

        Raises
        ------
        FileNotFoundError
            If the file doesnt exists
        """
        
        file_path = 'db/queries/select/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File {} doesn't exists".format(file_path))
    
    @classmethod
    def get_update_query(cls, file_name: str) -> str:
        """Get one query on db/queries/update

        Parameters
        ----------
        file_name : str
            Name of the file inside the path without the file extension
        
        Returns
        -------
            A string with the query in the file 

        Raises
        ------
        FileNotFoundError
            If the file doesnt exists
        """
        
        file_path = 'db/queries/update/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except:
            raise FileNotFoundError("File {} doesn't exists".format(file_path))

    @classmethod
    def get_insert_query(cls, file_name: str) -> str:
        """Get one query on db/queries/insert

        Parameters
        ----------
        file_name : str
            Name of the file inside the path without the file extension
        
        Returns
        -------
            A string with the query in the file

        Raises
        ------
        FileNotFoundError
            If the file doesnt exists
        """
        
        file_path = 'db/queries/insert/{}.sql'.format(file_name)
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except:
            raise FileNotFoundError("File {} doesn't exists".format(file_path))
    
    @classmethod
    def insert_register(cls, query_path: str, data: list) -> None:
        """
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query_path, data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_registers(cls, query_path: str, datas: list) -> None:
        """
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for data in datas:
            cursor.execute(query_path, data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def select_register(cls, query_path: str, data: list = []) -> list[set]:
        """
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        if data:
            cursor.execute(query_path, data)
        else:
            cursor.execute(query_path)
            
        exit_data = cursor.fetchall()

        conn.close()

        return exit_data

    @classmethod
    def delete_register(cls, query_path: str) -> None:
        """
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query_path)

        conn.close()    

        return None
    
    @classmethod
    def update_register(cls, query_path: str, data: list) -> None:
        """
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query_path, data)

        conn.commit()
        conn.close()    

        return None
            
    @classmethod
    @property
    def database_config(cls):
        return { 
            'user': 'tournament_user', 
            'host': 'localhost', 
            'password': 'tournament_pass', 
            'database': 'tournament' 
        }