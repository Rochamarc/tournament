import os

import mysql.connector
import json 

ABOVE_PATH = os.path.abspath(os.path.join(__file__, '../..'))

from alive_progress import alive_it

class BaseController:
    """
    Base class that contains every property and functions used in other controllers
    ...

    Attributes
    --------
    database_config
        A dict with database configuration

    Methods
    -------

    get_query(db_method: str, file_name: str)
        Get one query and returns as string
    insert_register(query: str, data: list)
        Make an insertion on database
    insert_registers(query: str, data: list)
        Make more than one insertion on database
    select_register(query: str, data: list = [])
        Make a selection on database
    delete_register(query: str)
        Make a delete on database
    update_register(query: str, data: list)
        Make an update on database
    check_register(query: str, data: list)
        Make a consult on database
    change_database(new_database: str):
        Change the database
    """

    database_pointer = 'mainDb'

    @classmethod
    def change_database_pointer(cls) -> None:
        """Switch the database automatically. Database options: main & test
        """

        option = ['mainDb', 'testDb']
        option.remove(cls.database_pointer)

        cls.database_pointer = option[0]
        
        print("Current Database: {}".format(cls.database_pointer))

        return None 
    
    @classmethod
    def database_config(cls) -> dict:
        """A dict containing all the database information, like: host, username, database_name & password"""
        with open(os.path.join(ABOVE_PATH, 'config.json')) as f:
            value : dict = json.load(f)[cls.database_pointer]

        return value
    
    @classmethod
    def get_query(cls, db_method: str, controller_name: str, file_name: str) -> str:
        """Get one query on db/queries/

        Parameters
        ----------
        db_method : str
            Name of the action that the user wanna made ex: select | insert | update | delete | check
        controller_name : str
            Name of the controller that goes inside the path
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
            ABOVE_PATH,
            'database',
            'tournament',
            'queries',
            db_method,
            controller_name,
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

        conn = mysql.connector.connect(**cls.database_config())
        cursor = conn.cursor()

        cursor.execute(query, data)
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_registers(cls, query: str, datas: list, complex: bool=True, progress_bar: bool=True) -> None:
        """Make multiple inserts on database

        Parameters
        ---------- 
        query : str
            A string containing an sql query
        data : list
            List containing the necessary data 
        complex : bool
            Bool for the complexity of the data, if the data is a list of list, leave marked as True else, insert False
        progress_bar : bool
            A bool value for the progress bar

        Returns
        -------
            None
        """

        conn = mysql.connector.connect(**cls.database_config())
        cursor = conn.cursor()

        if progress_bar:
            for data in alive_it(datas):    
                if complex:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query, [data])
        else:
            # skip alive progress

            for data in datas:
                if complex:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query, [data])


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

        conn = mysql.connector.connect(**cls.database_config())
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

        conn = mysql.connector.connect(**cls.database_config())
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

        conn = mysql.connector.connect(**cls.database_config())
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
        
        conn = mysql.connector.connect(**cls.database_config())
        cursor = conn.cursor()

        cursor.execute(query, data)
        
        exit_data = cursor.fetchall()

        conn.close()

        return exit_data

if __name__ == "__main__":
    ...