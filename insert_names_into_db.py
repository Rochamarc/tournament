import mysql.connector

db_config = {
    "user": "tournament_user",
    "password": "tournament_pass",
    "host": "localhost",
    "database": "tournament"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

with open('files/names/first_name_br.csv', 'r') as f:
    file = f.readlines()
    for n in file:
        cursor.execute("INSERT INTO first_names VALUES(NULL, %s, 'Portuguese');", [n.replace('\n','')])

with open('files/names/first_name_g.csv', 'r') as f:
    file = f.readlines()
    for n in file:
        cursor.execute("INSERT INTO first_names VALUES(NULL, %s, 'Spanish');", [n.replace('\n','')])


with open('files/names/last_name_br.csv', 'r') as f:
    file = f.readlines()
    for n in file:
        cursor.execute("INSERT INTO last_names VALUES(NULL, %s, 'Portuguese');", [n.replace('\n','')])

with open('files/names/last_name_g.csv', 'r') as f:
    file = f.readlines()
    for n in file:
        cursor.execute("INSERT INTO last_names VALUES(NULL, %s, 'Spanish');", [n.replace('\n','')])

conn.commit()
conn.close()