import sqlite3 

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
    avg REAL
);
    """)

    # stadium table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stadium ( 
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        location TEXT NOT NULL, 
        capacity INTEGER NOT NULL, 
        club_owner TEXT NOT NULL 
    ); 
    """)

    print("Tabelas criadas com sucesso!")

    conn.close() # close database

if __name__ == '__main__':
    create_db()