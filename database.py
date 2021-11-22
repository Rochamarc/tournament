import sqlite3
import os

database = 'database.db'

def create_db():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # player table
    cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    nationality TEXT NOT NULL,
    age INTEGER NOT NULL,
    overall INTEGER NOT NULL,
    current_club TEXT,
    position VARCHAR(30) NOT NULL,
    matches_played INTEGER,
    goals INTEGER,
    assists INTEGER,
    points REAL,
    avg REAL,
    save_file VARCHAR(30)
);
    """)

    # stadium table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stadium ( 
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        location TEXT NOT NULL, 
        capacity INTEGER NOT NULL, 
        club_owner TEXT  
    ); 
    """)

    # clubs_ranking table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clubs_ranking (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT NOT NULL,
        points REAL NOT NULL
    );
    """)

    print("Tabelas criadas com sucesso!")

    conn.close() # close database

# Upload conmebol ranking for the libertadores cup
def upload_ranking_db(verbose=False):
    
    os.system('clear')
    print("Inserindo ranking da conmebol na base de dados!")
    
    with open('ranking_conmebol.csv') as file:
        lines = file.readlines() 
    
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
    
        for line in lines:
            print('.', sep=' ', end=' ', flush=True)
            line = line.split(',')
            val = line[-1] 
            val.replace('\n', '')
            val = float(val)
            del line[-1]
            line.append(val)
    
            cursor.execute("""
            INSERT INTO clubs_ranking (name, country, points) VALUES (?,?,?)
            """, line)
    
            conn.commit()
        
        conn.close()

        if verbose : print("Ranking da conmebol inserido com sucesso!")

#
# Dometic Cup
#

def create_domestic_table(season, verbose=False):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    if verbose : print(f"Criando tabela da copa doméstica {season}")
    
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS campeonato_brasileiro_serie_a_{season} (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        club TEXT NOT NULL,
        matches INTEGER NOT NULL,
        won INTEGER NOT NULL,
        draw INTEGER NOT NULL,
        lost INTEGER NOT NULL,
        goals_for INTEGER NOT NULL,
        goals_away INTEGER NOT NULL,
        goal_diff INTEGER NOT NULL,
        points INTEGER NOT NULL
    );
    """)

    conn.close() # close database

    if verbose : print("Tabela criada com sucesso")


def domestic_table_basic(club_names,season, verbose=False):
    '''
    Insert club domestic cup data into the database
    '''

    os.system('clear')
    print("Inserting clubs into domestic cup table")
    
    for club in club_names:
        print('.', sep=' ', end=' ', flush=True)

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]
        
        if verbose : print(f"Inserting {club} into the database.")
        
        cursor.execute(f"INSERT INTO campeonato_brasileiro_serie_a_{season} (club, matches, won, draw, lost, goals_for, goals_away, goal_diff, points) VALUES (?,?,?,?,?,?,?,?,?)", ls)
        conn.commit()
        conn.close()

    os.system('clear')    
    if verbose : print("Database populada com sucesso!")
    
    return True 

def update_domestic_table(club_stats, season):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE campeonato_brasileiro_serie_a_{season} 
        SET matches=matches+1, 
            won=won + ?,
            draw=draw + ?,
            lost=lost + ?,
            goals_for=goals_for + ?,
            goals_away=goals_away + ?,
            goal_diff=goal_diff + ?,
            points=points + ?
        WHERE club = ?
    """, club_stats)
    
    conn.commit()
    conn.close()

def get_domestic_cup_table(season):
    ''' Get the domestic cup table data '''
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    val = cursor.execute(f"""
        SELECT * FROM campeonato_brasileiro_serie_a_{season} 
        ORDER BY 
            points DESC, 
            goals_for DESC, 
            goal_diff DESC
        """).fetchall()
    
    data = val.copy() # create a copy of the fetch data
    conn.close()
    
    return data
    
def get_players(club_name, verbose=False):
    ''' 
    Get the players info from database
    '''

    conn = sqlite3.connect(database)

    val = conn.execute("""
    SELECT * FROM players WHERE club=?
    """, club_name).fetchall() # fetch the result

    players_data = val.copy 
    conn.close() # close database 

    return players_data

def insert_players_db(players, verbose=False):
    '''
    Insert players data into the database
    '''

    os.system('clear')
    print("Inserting players on the database")
    
    for player in players:
        print('.', sep=' ', end=' ', flush=True)

        if verbose : print(f"Insert player {player} into the database")

        conn = sqlite3.connect(database)
        cursor = conn.cursor()        
        
        player_data = player.get_data()
        
        cursor.execute('''
            INSERT INTO players (name, nationality, age, overall, current_club, position, matches_played, goals, assists, points, avg)
            values (?,?,?,?,?,?,?,?,?,?,?)
        ''', player_data)

        conn.commit()
        conn.close()

    if verbose : print("Players inserted into the database sucessfully!")
    return True
    
if __name__ == '__main__':
    create_db()
    upload_ranking_db()
