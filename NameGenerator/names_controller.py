import sys
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from NameGenerator.base_controller import BaseController

import mysql.connector

from alive_progress import alive_it

class NamesController(BaseController):
    """
    Class that handle tournament_name database

    Methods
    -------
    insert_first_names(first_names: list, nationality: str)
        Insert first names in database
    insert_last_names(last_names: list, nationality: str)
        Insert last names in database
    select_first_names(nationality: str)
        Select a list of first names in database
    select_last_names(nationality: str)
        Select a list of last names in database
    select_full_name_by_nationality(nationality: str)
        Select a random full name by nationality
    """
    
    @classmethod
    def insert_first_names(cls, first_names: list, nationality: str) -> None:
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
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for first_name in alive_it(first_names):
            cursor.execute(cls.get_query('insert','insert_first_names'), [first_name, nationality])
        
        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_last_names(cls, last_names: list, nationality: str) -> None:
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

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        for last_name in alive_it(last_names):
            cursor.execute(cls.get_query('insert','insert_last_names'), [last_name, nationality])
        
        conn.commit()
        conn.close()

        return None 

    @classmethod
    def select_first_names(cls, nationality: str) -> list:
        """Select first names from tournament_name.first_names
        
        Parameters
        ----------
        nationality : str
            Str used to select the nationality of first names
        
        Returns
        -------
            A list of lists with first names 
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_names'), [nationality])
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def select_last_names(cls, nationality: str) -> list:
        """Select last names from tournament_name.last_names
        
        Parameters
        ----------
        nationality : str
            Str used to select the nationality of last names
        
        Returns
        -------
            A list of lists with last names 
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_last_names'), [nationality])
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def select_full_name_by_nationality(cls, nationality: str) -> list[set]:
        """Select a random name from tournament_name.first_names & tournament_name.last_names 
        
        Parameters
        ----------
        nationality : str
            Str used to select the nationality of the name
        
        Returns
        -------
            A two dimentional list with first name and last name 
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_random_name_by_nationality'), [nationality, nationality])
        res = cursor.fetchall()

        conn.close()

        return res