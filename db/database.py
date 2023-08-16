import mysql.connector

from db.open_query import QueryHelper 

qh = QueryHelper()

config = {
    'user': 'tournament_user', 
    'host': 'localhost', 
    'password': 'tournament_pass',
    'database': 'tournament_db'
}

def export_database_config() -> dict:
    ''' Return a dict with database configuration '''
    return config

def export_conn() -> mysql.connector:
    ''' Return a mysql connector '''
    conn = mysql.connector.connect(**config)

    return conn

def create_db() -> None:
    ''' Connect to a database and execute creation queries '''
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    
    # execute a query
    cursor.execute(qh.open_create_query('brasileirao').format('serie_a', '2021')) # exemplo
    cursor.execute(qh.open_create_query('champions'))
    cursor.execute(qh.open_create_query('clubs'))
    cursor.execute(qh.open_create_query('clubs_ranking'))
    cursor.execute(qh.open_create_query('coaches'))
    # cursor.executqh.e(open_create_query('libertadores')) 
    cursor.execute(qh.open_create_query('players'))
    cursor.execute(qh.open_create_query('players_season'))
    cursor.execute(qh.open_create_query('retirees'))
    cursor.execute(qh.open_create_query('stadiums'))
    # conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()