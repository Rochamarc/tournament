import sqlite3
import os

database = 'database.db'

def create_db():
    ''' Create database tables '''
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # create player table
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

    # create stadium table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stadium ( 
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        location TEXT NOT NULL, 
        capacity INTEGER NOT NULL, 
        club_owner TEXT  
    ); 
    """)

    # create conmebom ranking table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clubs_ranking (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT NOT NULL,
        points REAL NOT NULL
    );
    """)

    print("Tabelas criadas com sucesso!")

    conn.close()


def upload_ranking_db(verbose=False):
    ''' Upload conmebol ranking '''    
    
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



class DomesticLeague():

    @staticmethod
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
    
    @staticmethod
    def domestic_table_basic(club_names,season, verbose=False):
        '''
        Insert club domestic cup data into the database
        '''

        
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

            
        if verbose : print("Database populada com sucesso!")

        return True 

    @staticmethod
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

    @staticmethod
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

class InternationalCup():

    @staticmethod
    def create_international_cup(season, group, verbose=False):
        ''' Create international cup table '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        if verbose : print(f"Criando tabela da copa doméstica {season} {group}")

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS libertadores_{group}_{season} (
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

    @staticmethod
    def update_international_table(club_stats, group, season):
        ''' Insert into the international cup table '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(f"""
            UPDATE libertadores_{group}_{season} 
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

    @staticmethod
    def international_group_table_basic(club_names,season, group, verbose=False):
        '''
        Basic international cup data
        '''

        print("Inserting clubs into domestic cup table")

        for club in club_names:
            print('.', sep=' ', end=' ', flush=True)

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()


            ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]

            if verbose : print(f"Inserting {club} into the database.")

            cursor.execute(f"INSERT INTO libertadores_{group}_{season} (club, matches, won, draw, lost, goals_for, goals_away, goal_diff, points) VALUES (?,?,?,?,?,?,?,?,?)", ls)
            conn.commit()
            conn.close()
    
        if verbose : print("Database populada com sucesso!")

    @staticmethod
    def get_group_stage_data(season):
        ''' 
        Get international cup group stage 
        return dict { 'A' : [data], ... }
        '''

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        full_data = {}

        for group in groups:
            g = f'group_{group}'

            val = cursor.execute(f"""
                SELECT * FROM libertadores_{g}_{season}
                ORDER BY 
                    points DESC, 
                    goals_for DESC, 
                    goal_diff DESC
                """).fetchall()

            data = val.copy() # create a copy of the fetch data
            full_data[group] = data
        conn.close()
        
        return full_data

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
            INSERT INTO players (name, nationality, age, overall, current_club, position, matches_played, goals, assists, avg)
            values (?,?,?,?,?,?,?,?,?,?)
        ''', player_data)

        conn.commit()
        conn.close()

    if verbose : print("Players inserted into the database sucessfully!")
    return True
    
if __name__ == '__main__':
    create_db()
    upload_ranking_db()
