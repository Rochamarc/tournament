from classes import *
from name_nationality import *

class GenerateClass:
    @staticmethod
    def set_players(club_name, country, coeff, skip_db=True):
        ''' Generate players <class 'Player'> to the club <class 'Club'> 
            return a dict 
        '''

        shirt_numbers = [ x for x in range(1,50) ]
    
        squad = {
            'goal_keeper': [],
            'defender': [],
            'midfielder': [],
            'attacker': []
        }

        for _ in range(3):
            natio_ = generate_nationality(country)
            name_ = generate_name(natio_) 
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad['goal_keeper'].append(Player(name_, natio_, randint(16,37), 'Goalkeeper', current_club=club_name, shirt_number=number, club_coeff=coeff))
        for _ in range(12):
            natio_ = generate_nationality(country)
            name_ = generate_name(natio_) 
            pos_ = choice(['Center Back', 'Left Back', 'Right Back'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad['defender'].append(Player(name_, natio_, randint(16,37), pos_,  current_club=club_name, shirt_number=number, club_coeff=coeff))
        for _ in range(12):
            natio_ = generate_nationality(country)
            name_ = generate_name(natio_) 
            pos_ = choice(['Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad["midfielder"].append(Player(name_, natio_, randint(16,37), pos_,  current_club=club_name, shirt_number=number, club_coeff=coeff))
        for _ in range(6):
            natio_ = generate_nationality(country)
            name_ = generate_name(natio_) 
            pos_ = choice(['Center Forward', 'Second Striker', 'Winger'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad["attacker"].append(Player(name_, natio_, randint(16,37), pos_,  current_club=club_name, shirt_number=number, club_coeff=coeff))

        if not skip_db:
            # registrate on the database
            print("Inserting players into database")
            for player in squad["goal_keeper"]:
                player.db_insertion()
            for player in squad['defender']:
                player.db_insertion()
            for player in squad['midfielder']:
                player.db_insertion()
            for player in squad['attacker']:
                player.db_insertion()
            print("Insertion completed sucessfully!")

        return squad 


