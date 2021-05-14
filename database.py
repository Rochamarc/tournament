import sqlite3 
from ranking import Ranking

r = Ranking()

def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # player table
    cursor.execute("""
CREATE TABLE IF NOT EXISTS player (
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

if __name__ == '__main__':
    create_db()
    r.upload_ranking_db()
