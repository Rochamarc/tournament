import sqlite3
from alive_progress import alive_bar
from open_query import QueryHelper

import sys

args = sys.argv

qh = QueryHelper()

if len(args) > 1:
    database = f'db/{args[-1]}.db'
else:
    database = 'db/database.db'

def create_db():
    ''' Create database tables '''
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    with alive_bar(1) as bar:
        cursor.execute(qh.open_create_query('players'))
        cursor.execute(qh.open_create_query('coaches')) 
        cursor.execute(qh.open_create_query('stadiums'))
        cursor.execute(qh.open_create_query('clubs_ranking'))
        cursor.execute(qh.open_create_query('games'))
        cursor.execute(qh.open_create_query('clubs'))
        cursor.execute(qh.open_create_query('champions'))
        cursor.execute(qh.open_create_query('retirees'))
        cursor.execute(qh.open_create_query('players_season'))
        bar()

    conn.close()


def upload_ranking_db():
    ''' Upload conmebol ranking '''    
    
    with open('files/conmebol/ranking_conmebol.csv', encoding='utf8') as file:
        lines = file.readlines() 
    
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
    
        for line in lines:
            line = line.split(',')
            val = line[-1] 
            val.replace('\n', '')
            val = float(val)
            del line[-1]
            line.append(val)
    
            cursor.execute(qh.open_insert_query('clubs_ranking'), line)
    
        conn.commit()
        conn.close()


if __name__ == '__main__':
    create_db()
    upload_ranking_db()
 