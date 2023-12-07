import os
import pathlib

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()

class BaseController:
    """
    Base class that contains every property and functions used in other controllers
    """
    
    @classmethod
    def get_select_query(cls, file_name: str) -> str:
        """Get one query on queries/select

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
        
        # 'NameGenerator/queries/select/{}.sql'.format(file_name)

        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            'select',
            f'{file_name}.sql'
            )
        
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File {} doesn't exists".format(file_path))

    @classmethod
    def get_insert_query(cls, file_name: str) -> str:
        """Get one query on queries/insert

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
            f'{file_name}.sql'
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
            'database': 'tournament_name' 
        }