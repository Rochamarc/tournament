import mysql.connector
from random import choice, randint, shuffle, uniform

from NameGenerator.names_controller import NamesController
from db.clubs_controller import ClubsController
from db.overall_controller import OverallController
from db.players_controller import PlayersController
from db.player_contracts_controller import PlayerContractsController

clubs_controller = ClubsController()
names_controller = NamesController()
overall_controller = OverallController()
players_controller = PlayersController()
player_contracts_controller = PlayerContractsController()

# CREATE PLAYERS AND PLAYERS CONTRACT

# Suport lists
gk = ['GK']
df = ['LB', 'RB', 'CB']
mf = ['DM', 'CM', 'RM', 'LM', 'AM' ]
at = ['SS', 'WG', 'CF' ]

countries = ['Argentina', 'Colombia', 'Uruguay', 'Paraguay', 'Chile']

# Select brazilian first & last names
nationality = "portuguese br"

br_first_names = names_controller.select_first_names(nationality)
br_last_names = names_controller.select_last_names(nationality)

# Select spanish first & last names
nationality = 'spanish'

g_first_names = names_controller.select_first_names(nationality)
g_last_names = names_controller.select_last_names(nationality)

# Select clubs names and id
clubs = clubs_controller.select_id_name()

# Create and insert a list of players data and insert into database
for club in clubs:
    club_id = club[0]
    n_for_player = { 'GK': 3, 'DF': 9, 'MF': 11, 'AT': 7 }

    # for position, number_of_players_per_position
    for ps, n_ps in n_for_player.items():
        # Player creation block 
        
        for _ in range(n_ps):
            if ps == 'GK':
                position = 'GK'
                height = round(uniform(1.87, 1.99), 2)
            elif ps == 'DF':
                position = choice(df)
                height = round(uniform(1.80, 1.90), 2)
            elif ps == 'MF':
                position = choice(mf)
                height = round(uniform(1.60, 1.90), 2)
            elif ps == 'AT':
                position = choice(at)
                height = round(uniform(1.60, 1.95), 2)
            else:
                position = None

            weight = round(uniform(60.0, 90.9), 2)
            foot = choice(['R','L'])
            birth = str(randint(1984,2006))
    
            gringo_chance = randint(1,10)

            # 3 chances in 10 of a gringo player
            if gringo_chance in [1,5,9]:
                nationality = choice(countries)
                name = ' '.join([choice(g_first_names)[0], choice(g_last_names)[0]]) 
            else: 
                nationality = 'Brazil'
                name = ' '.join([choice(br_first_names)[0], choice(br_last_names)[0]])
                 
            # insert player into database
            players_controller.insert_players([[name, nationality, position, birth, height, weight, foot ]])
            
            # end of player insertion 

    # Select the 30 last players created and insert a contract between a club and player
    last_players = players_controller.select_last_players()

    for player in last_players:
        # cursor.execute(insert_contract, ['2022','2026', 100_000, club_id, player[0]])
        player_contracts_controller.insert_player_contracts([ [ '2022', '2026', 100_000, club_id, player[0] ] ])
    

# INSERT PLAYERS OVERALL

# Queries
# select_players_id

# insert a players overall table with 
season = '2022'

# Select players id
players = players_controller.select_all_players_id()

# Create and insert data into database 

for player in players:
    id = player[0]
    overall = randint(50,90)
    # cursor.execute(insert_players_overall, [overall, id])
    overall_controller.insert_overall([ [season, overall, id] ])

# CREATE COACHES

# Database configuration and connection
db_config['database'] = 'tournament_name'

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Queries 
select_clubs_id = "SELECT id FROM clubs;" 

insert_coaches = "INSERT INTO coaches VALUES(NULL, %s, %s, %s)"

select_random_first_name = 'SELECT first_names.value FROM first_names ORDER BY RAND() LIMIT 1';
select_random_last_name = 'SELECT last_names.value FROM last_names ORDER BY RAND() LIMIT 1';

# Change databse and reconnect and create a new cursor 
db_config['database'] = 'tournament'

conn2 = mysql.connector.connect(**db_config)
cursor2 = conn2.cursor()

# Create a list of countries to be coach.nationality
countries = ['Brazil', 'Chile', 'Argentina', 'Uruguay', 'Portugal', 'Paraguay', 'Colombia', 'Venezuela' ]

# Select clubs id
cursor2.execute(select_clubs_id)
clubs = cursor2.fetchall()

# Create coaches and insert into the database 
for c in clubs:
    cursor.execute(select_random_first_name) # select a random first name
    f = cursor.fetchall()

    cursor.execute(select_random_last_name) # select a random last name
    l = cursor.fetchall()
    
    name = ' '.join([f[0][0], l[0][0]]) # define the name    
    
    nationality = choice(countries) # nationality
    
    birth = str(randint(1950, 1979)) # birth

    cursor2.execute(insert_coaches, [name, nationality, birth])

conn2.commit()    

# COACHES CONTRACTS 

# Queries 
insert_contract = "INSERT INTO coach_contracts (start, end, salary, club_id, coach_id) VALUES(%s, %s, %s, %s, %s);"
select_coaches = "SELECT id FROM coaches;"
select_clubs = "SELECT id FROM clubs"

# Coaches creation clauses
start = '2022'
end = '2026'
salary = 100_000

# Select coaches and clubs
cursor2.execute(select_coaches)
coaches = cursor2.fetchall()

cursor2.execute(select_clubs)
clubs = cursor2.fetchall()

# Shuffle the data
shuffle(coaches)
shuffle(clubs)

# Create and inser data into the database

for _ in range(len(coaches)):
    club_id = clubs.pop()[0]
    coach_id = coaches.pop()[0]

    cursor2.execute(insert_contract, [start, end, salary, club_id, coach_id])
conn2.commit()

conn2.close()
conn.close()