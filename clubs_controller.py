import mysql.connector

database_config = {
    'user': 'tournament_user',
    'password': 'tournament_pass',
    'host': 'localhost',
    'database': 'football'
}


class ClubsController:
    @staticmethod
    def select_clubs_by_country(country: str) -> list[set]:
        ''' Returns a list of clubs on the database by clubs.country clause '''
        
        conn = mysql.connector.connect(**database_config)
        cursor = conn.cursor()

        select_clubs_query = """
        SELECT clubs.id, clubs.name, clubs.country, clubs.class, confederations.name 
        FROM clubs 
        INNER JOIN confederations 
            ON confederations.id = clubs.id_confederation 
        WHERE clubs.country = '{}';"""

        cursor.execute(select_clubs_query.format(country))
        clubs = cursor.fetchall()

        conn.close()

        return clubs 
    
if __name__ == "__main__":
    print(ClubsController().select_clubs_by_country('Brazil'))