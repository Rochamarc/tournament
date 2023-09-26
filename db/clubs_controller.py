import mysql.connector
from db.base_controller import BaseController

class ClubsController(BaseController):
    @classmethod
    def select_serie_a_clubs(cls) -> list[set]:
        ''' Returns a list of clubs based on divison 

            warning: this will receive an argument season that have 
            a clause inside the query
        '''
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_serie_a_clubs'))
        clubs = cursor.fetchall()

        conn.close()
        return clubs 

    @classmethod
    def select_serie_b_clubs(cls) -> list[set]:
        ''' Returns a list of clubs based on divison 

            warning: this will receive an argument season that have 
            a clause inside the query
        '''
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_serie_b_clubs'))
        clubs = cursor.fetchall()

        conn.close()
        return clubs 
    

    @classmethod
    def select_serie_c_clubs(cls) -> list[set]:
        ''' Returns a list of clubs based on divison 

            warning: this will receive an argument season that have 
            a clause inside the query
        '''
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_select_query('select_serie_c_clubs'))
        clubs = cursor.fetchall()

        conn.close()
        return clubs 
    
if __name__ == "__main__":
    print(ClubsController().select_serie_a_clubs())