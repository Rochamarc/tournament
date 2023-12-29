import os
import pathlib

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()

# TODO refact all that get_query to just one receiving the method => insert, update, delete, etc

import mysql.connector


class BaseController:
    """
    Base class that contains every property and functions used in other controllers
    """

    @classmethod
    def get_check_query(cls, file_name: str) -> str:
        """Get one query on db/queries/check

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

        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            'check',
            '{}.sql'.format(file_name)            
        )

        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File {} doesn't exists".format(file_path))

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

        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            'delete',
            '{}.sql'.format(file_name)            
        )

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
        
        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            'select',
            '{}.sql'.format(file_name)            
        )

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

        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            'update',
            '{}.sql'.format(file_name)            
        )
        
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

        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            'insert',
            '{}.sql'.format(file_name)            
        )
        
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except:
            raise FileNotFoundError("File {} doesn't exists".format(file_path))
    
    @classmethod
    def insert_register(cls, query: str, data: list) -> None:
        """Make an insert on database

        Parameters
        ---------- 
        query : str
            A string containing an sql query
        data : list
            List containing data 

        Returns
        -------
            None        
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query, data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_registers(cls, query: str, datas: list) -> None:
        """Make multiple inserts on database

        Parameters
        ---------- 
        query : str
            A string containing an sql query
        data : list
            List containing the necessary data 

        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for data in datas:
            cursor.execute(query, data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def select_register(cls, query: str, data: list = []) -> list[set]:
        """Make a select on database

        Parameters
        ---------- 
        query : str
            A string containing an sql query
        data : list
            List containing data if necessary, default value is an empty list [] 

        Returns
        -------
            A list with of sets
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
            
        exit_data = cursor.fetchall()

        conn.close()

        return exit_data

    @classmethod
    def delete_register(cls, query: str) -> None:
        """Make a delete on database

        Parameters
        ---------- 
        query : str
            A string containing an sql query
    
        Returns
        -------
            A list with of sets
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query)

        conn.close()    

        return None
    
    @classmethod
    def update_register(cls, query: str, data: list) -> None:
        """Make a update on database

        Parameters
        ---------- 
        query : str
            A string containing an sql query
        data : list
            List containing the necessary data

        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query, data)

        conn.commit()
        conn.close()    

        return None
    
    @classmethod
    def check_register(cls, query: str, data: list) -> list[set]:
        """Make a check in the database based on the business rule.
        Use this to find if theres data located on table or with a parameter
        that cant be double. If there's data raise an error.

        Parameters
        ----------
        query : str
            A string containing a query located on db/queries/check
        data : list
            A list with necessary data
        
        Returns
        -------
            A list of sets if there's data where the check is going on, Otherwise will returns an empty
            list
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(query, data)
        
        exit_data = cursor.fetchall()

        conn.close()

        return exit_data
    

    @classmethod
    @property
    def database_config(cls):
        """Return a dict with database configuration, change the user,
        host and password based on database 
        """
        
        return { 
            'user': 'tournament_user', 
            'host': 'localhost', 
            'password': 'tournament_pass', 
            'database': 'tournament' 
        }