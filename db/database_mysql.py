import mysql.connector


#### PROVISORIO
import os 

def change_directory(func):
    def wrapper(*args): 
        original_dir = os.getcwd()
        os.chdir(r'{}/db/query_my_sql/'.format(os.getcwd()))
        
        s = func(args[0]) 
    
        os.chdir(original_dir)

        return s 
    return wrapper

@staticmethod
@change_directory
def open_create_query(query: str) -> str:
    ''' Prepare and return the string for the create query '''
    s = None
    
    with open('create/create_{}'.format(query), 'r') as f:
        s = f.readlines()[0].replace('\n', '')
    
    return s


config = {
    'user': 'tournament_user', 
    'host': 'localhost', 
    'password': 'tournament_pass',
    'database': 'tournament_db'
}

conn = mysql.connector.connect(**config)

# print(conn)

cursor = conn.cursor()

# execute a query
# cursor.execute(open_create_query('brasileirao').format('serie_a', '2021')) # exemplo
cursor.execute(open_create_query('champions'))
cursor.execute(open_create_query('clubs'))
cursor.execute(open_create_query('clubs_ranking'))
cursor.execute(open_create_query('coaches'))
# cursor.execute(open_create_query('libertadores')) 
cursor.execute(open_create_query('players'))
cursor.execute(open_create_query('players_season'))
cursor.execute(open_create_query('retirees'))

# conn.commit()
conn.close()