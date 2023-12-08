import os
import pathlib

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()

# TODO refact all that get_query to just one receiving the method => insert, update, delete, etc

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
    @property
    def database_config(cls):
        return { 
            'user': 'tournament_user', 
            'host': 'localhost', 
            'password': 'tournament_pass', 
            'database': 'tournament' 
        }