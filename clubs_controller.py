import mysql.connector
from base_controller import BaseController

class ClubsController(BaseController):
    @classmethod
    def select_clubs_by_country(cls, country: str) -> list[set]:
        ''' Returns a list of clubs on the database by clubs.country clause '''
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select_clubs_by_country'), [country])
        clubs = cursor.fetchall()

        conn.close()
        return clubs 
    
if __name__ == "__main__":
    print(ClubsController().select_clubs_by_country('Brazil'))