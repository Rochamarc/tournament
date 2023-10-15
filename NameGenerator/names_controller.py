import mysql.connector

database_config = {
    'user': 'tournament_user',
    'password': 'tournament_pass',
    'database': 'tournament_name',
    'host': 'localhost'
}

class NamesController:
    @staticmethod
    def insert_first_names(first_names: list, nationality: str) -> None:
        ''' Insert names into the tournament_name.first_names '''
        conn = mysql.connector.connect(**database_config)
        cursor = conn.cursor()

        for first_name in first_names:
            cursor.execute('INSERT INTO first_names VALUES(NULL, %s, %s);', [first_name, nationality])
        
        conn.commit()
        conn.close()

        return None

    @staticmethod
    def insert_last_names(last_names: list, nationality: str) -> None:
        ''' '''
        conn = mysql.connector.connect(**database_config)
        cursor = conn.cursor()

        for last_name in last_names:
            cursor.execute('INSERT INTO last_names VALUES(NULL, %s, %s);', [last_name, nationality])
        
        conn.commit()
        conn.close()

        return None 