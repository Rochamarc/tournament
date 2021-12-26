import sqlite3


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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        competition TEXT NOT NULL,
        season TEXT NOT NULL,
        hour TEXT NOT NULL,
        home_team TEXT NOT NULL,
        away_team TEXT NOT NULL,
        score TEXT NOT NULL,
        stadium TEXT NOT NULL,
        home_shots INTEGER NOT NULL,
        home_shots_on_target INTEGER NOT NULL,
        home_fouls INTEGER NOT NULL, 
        home_tackles INTEGER NOT NULL,
        home_saves INTEGER NOT NULL,
        home_ball_possession INTEGER NOT NULL,
        home_offsides INTEGER NOT NULL,
        home_freekicks INTEGER NOT NULL,
        away_shots INTEGER NOT NULL,
        away_shots_on_target INTEGER NOT NULL,
        away_fouls INTEGER NOT NULL,
        away_tackles INTEGER NOT NULL,
        away_saves INTEGER NOT NULL,
        away_ball_possession INTEGER NOT NULL,
        away_offsides INTEGER NOT NULL,
        away_freekicks INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT NOT NULL,
        state TEXT NOT NULL,
        coeff INTEGER NOT NULL,
        club_class VARCHAR(1) NOT NULL,
        formation TEXT
    );
    """)

    print("Tabelas criadas com sucesso!")

    conn.close()


def upload_ranking_db(verbose=False):
    ''' Upload conmebol ranking '''    
    
    
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
    def create_domestic_table(division, season, verbose=False):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        division.replace(' ', '_')

        if verbose : print(f"Criando tabela da copa doméstica {division} {season}")

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS campeonato_brasileiro_{division}_{season} (
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
    def domestic_table_basic(club_names, division, season, verbose=False):
        '''
        Insert club domestic cup data into the database
        '''

        division.replace(' ', '_')
        
        print("Inserting clubs into domestic cup table")

        for club in club_names:
            print('.', sep=' ', end=' ', flush=True)

            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            ls = [club, 0, 0, 0, 0, 0, 0, 0, 0]

            if verbose : print(f"Inserting {club} into the database.")

            cursor.execute(f"INSERT INTO campeonato_brasileiro_{division}_{season} (club, matches, won, draw, lost, goals_for, goals_away, goal_diff, points) VALUES (?,?,?,?,?,?,?,?,?)", ls)
            conn.commit()
            conn.close()

            
        if verbose : print("Database populada com sucesso!")

        return True 

    @staticmethod
    def update_domestic_table(club_stats, division, season):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        division.replace(' ', '_')

        cursor.execute(f"""
            UPDATE campeonato_brasileiro_{division}_{season} 
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
    def get_domestic_cup_table(division, season):
        ''' Get the domestic cup table data '''
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute(f"""
            SELECT * FROM campeonato_brasileiro_{division}_{season} 
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


class ClubData():
    @staticmethod
    def insert_clubs_db(clubs, verbose=False):
        '''
        Insert clubs into the databse
        '''

        print('Inserting clubs into the database')

        for club in clubs:
            print('.', sep=' ', end=' ', flush=True)

            if verbose : print(f"Insert club {club} into the database")

            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            club_data = club.get_data()

            cursor.execute("INSERT INTO clubs (name, country, state, coeff, club_class, formation) values (?,?,?,?,?,?)", club_data)
            
            conn.commit()
            conn.close()

        if verbose : print("Players inserted into the database sucessfully!")
        return True

    @staticmethod
    def get_clubs(club_name, verbose=False):
        ''' Get clubs info from database '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute("SELECT * FROM clubs WHERE name=?", (club_name, )).fetchall() 

        data = val.copy()
        conn.close()

        return data


class PlayerData():
    @staticmethod
    def get_players(club_name, verbose=False):
        ''' 
        Get the players info from database
        '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute("SELECT * FROM players WHERE current_club=?", (club_name, ) ).fetchall() # fetch the result

        data = val.copy()
        conn.close() # close database 

        return data

    @staticmethod
    def insert_players_db(players, verbose=False):
        '''
        Insert players data into the database
        '''


        print("Inserting players on the database")

        for position, players in players.items():
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

    @staticmethod
    def update_player_stats(player_list, verbose=False):
        for player in player_list:
            print('.', sep=' ', end=' ', flush=True)
            
            player_data = player.get_competition_stats()

            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            if verbose : print(f"Update {player}")

            cursor.execute(f"""
                UPDATE players 
                SET matches_played=matches_played+?, 
                    goals=goals+?,
                    assists=assists+?,
                    points=points+?
                WHERE id = ?
            """, player_data)

            conn.commit()
            conn.close()

        if verbose : print("Player updated sucessfully!")
        return True

class StadiumData():
    @staticmethod
    def insert_stadiums_db(stadiums, verbose=False):
        ''' Insert stadiums to the database '''
        
        print("Inserting stadiums into the database ")

        for stadium in stadiums:
            print('.', sep=' ', end=' ', flush=True)

            if verbose : print(f"Insert stadium {stadium} into the database")

            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            std_data = stadium.get_data()

            cursor.execute("INSERT INTO stadium (name, location, capacity, club_owner) VALUES (?,?,?,?)", std_data)

            conn.commit()
            conn.close()

        if verbose : print("Stadiums inserted into the database sucessfully!")
        return True

    @staticmethod
    def get_stadiums():
        ''' Get stadiums data '''

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        val = cursor.execute("SELECT name, location, capacity, club_owner FROM stadium").fetchall()

        data = val.copy()
        conn.close()

        return data 

class GameData():
    @staticmethod
    def insert_games_db(game_list, verbose=False):
        ''' 
            Insert game data into database 

            below the order to receive the data 
            [ competition, season, hour, home_team, away_team, score, stadium, home_shots, home_shots_on_target, home_fouls, 
            home_tackles, home_saves, home_ball_possession, home_offsides, home_freekicks, away_shots, away_shots_on_target,
            away_fouls, away_tackles, away_saves, away_ball_possession, away_offsides, away_freekicks ]
        '''
        
        for game in game_list:
            print('.', sep=' ', end=' ', flush=True)

            if verbose : print(f"Inserting game {game} on the database")

            game_data = game.data()

            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO game (
                competition,
                season,
                hour,
                home_team,
                away_team,
                score,
                stadium,
                home_shots,
                home_shots_on_target,
                home_fouls,
                home_tackles,
                home_saves,
                home_ball_possession,
                home_offsides,
                home_freekicks,
                away_shots,
                away_shots_on_target,
                away_fouls,
                away_tackles,
                away_saves,
                away_ball_possession,
                away_offsides,
                away_freekicks
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, game_data)

            conn.commit()
            conn.close()

        if verbose : print("Game data inserted sucessfully")

        return True
    
if __name__ == '__main__':
    create_db()
    upload_ranking_db()
