from NameGenerator.names_controller import NamesController

from random import randint, shuffle

from controllers.coaches_controller import CoachesController
from controllers.clubs_controller import ClubsController
from controllers.players_controller import PlayersController

from data_generator import calculate_market_value, calculate_overall_per_player
from data_generator import generate_height_and_position, generate_name_nationality
from data_generator import generate_player_contracts, generate_players_skills
from data_generator import generate_weight_foot_and_birth

from data_manipulation import formulate_data_for_market_value

from alive_progress import alive_it


clubs_controller = ClubsController()
coaches_controller = CoachesController()
names_controller = NamesController()
players_controller = PlayersController()

# TODO this cannot be a constant
# this has to be a variable
season = '2022'

countries = ['Argentina', 'Colombia', 'Uruguay', 'Paraguay', 'Chile']

# Select brazilian first & last names
nationality = "portuguese br"

br_first_names = names_controller.select_first_names(nationality)[0]
br_last_names = names_controller.select_last_names(nationality)[0]

# Select spanish first & last names
nationality = 'spanish'

g_first_names = names_controller.select_first_names(nationality)[0]
g_last_names = names_controller.select_last_names(nationality)[0]

# Select clubs names and id
clubs = clubs_controller.select_id_name_class()

# Create and insert a list of players data and insert into database
print("Creating Players")

for club in alive_it(clubs):
    club_id = club[0]
    club_class = club[-1]

    n_for_player = { 'GK': 3, 'DF': 9, 'MF': 11, 'AT': 7 }

    players_data = []

    # iterate player_functions by number of player_functions
    for player_funtion, n_player_function in n_for_player.items():
        
        # Player creation block 
        for _ in range(n_player_function):
            # Generate players body info
            position, height = generate_height_and_position(player_funtion)
            weight, foot, birth = generate_weight_foot_and_birth()  

            # 3 chances in 10 of a gringo player
            name, nationality = generate_name_nationality(countries, br_first_names, br_last_names, g_first_names, g_last_names)
    
            # Players data by club
            players_data.append([
                name, 
                nationality, 
                position, 
                birth, 
                height, 
                weight, 
                foot 
            ])
            
    # Insert 30 players into database
    players_controller.insert_players(players_data)

    # Select last 30 last player from database
    last_players = players_controller.select_last_players()
    
    # Inserting player's skills
    print(f"Creating & Saving Player Skills from {club[1]}")
    skills_data = generate_players_skills(last_players, club_class)

    # insert the skills per season     
    players_controller.insert_skills(skills_data, season)
    
    # select last skills
    last_skills = players_controller.select_last_skills(season)
    
    # here we create the market_value

    # calculate the average of overall
    # here we have a list of overalls and player_id
    players_overall_data = calculate_overall_per_player(last_skills)

    # formulate market value pre data
    mk_value_formulate = formulate_data_for_market_value(last_players, players_overall_data)
    market_value_data = calculate_market_value(mk_value_formulate, season)

    # insert market value on database
    players_controller.insert_players_market_value(market_value_data)

    # Generate player contracts
    player_contracts = generate_player_contracts(last_players, club_id, season)

    # Insert player contracts on database
    players_controller.insert_player_contracts(player_contracts)
    

# CREATE COACHES

# Create a list of countries to be coach nationality
# countries = ['Brazil', 'Chile', 'Argentina', 'Uruguay', 'Portugal', 'Paraguay', 'Colombia', 'Venezuela' ]


# Select clubs id
clubs = clubs_controller.select_id()

# Create coaches and insert into the database 

print("Creating Coaches")
coaches = []
for _ in alive_it(clubs):
    # Select the name
    name = names_controller.select_full_name_by_nationality('portuguese br') 
    
    # Define coach info    
    nationality = 'Brazil' 
    birth = str(randint(1950, 1979)) 

    # Coaches data
    coaches.append([
        name[0][0], 
        nationality, 
        birth
    ])

print("Inserting Coaches")
coaches_controller.insert_coaches(coaches)

# COACHES CONTRACTS 

# Coaches creation clauses
start = '2022'
end = '2026'
salary = 100_000

# Select coaches and clubs
coaches = coaches_controller.select_id()
clubs = clubs_controller.select_id()

# Shuffle the data
shuffle(coaches)
shuffle(clubs)

# Create and inser data into the database

print("Creating Coach Contracts")

coach_contracts = []
for _ in alive_it(range(len(clubs))):
    club_id = clubs.pop()
    coach_id = coaches.pop()[0]

    coach_contracts.append([start, end, salary, club_id, coach_id])

print("Inserting Coach Contracts")
coaches_controller.insert_coach_contracts(coach_contracts)
