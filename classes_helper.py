from classes import *
from name_nationality import NameAndNationality as name_and_nat

# Tera um methodo de criar stadios e salvar na db
# Tera um metodo de gerar 32 clubs aleatoriamente
#
#
#

Name = name_and_nat()

class GenerateClass:
    @staticmethod
    def update_player_stats(clubs):
        ''' Update players stats return None '''

        for club in clubs:
            for player in club.start_eleven : player.set_avg() # update average
            for player in club.bench : player.set_avg() # update average

        return None 

    @staticmethod 
    def set_clubs(clubs_dict):
        ''' Generate a list of clubs <class 'Club'> 
            return a list(clubs)
        '''

        clubs = []

        # Creating a save file
        save_file = None # = input("Digite um valor de ate 30 caracteres pra criar um save file: ")

        if not save_file:
            save_file = None

        for club, country in clubs_dict.items():
            c = Club(club, country, save_file=save_file)
            # c.set_squad(skip_db=True)
            sq = GenerateClass().set_players(c.name, c.country, c.coeff) # this will generate the club squad
            c.set_formation(sq)
            clubs.append(c)

        return clubs 

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
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad['goal_keeper'].append(Player(name_, natio_, randint(16,37), 'Goalkeeper', current_club=club_name, shirt_number=number, club_coeff=coeff))
        for _ in range(12):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['Center Back', 'Left Back', 'Right Back'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad['defender'].append(Player(name_, natio_, randint(16,37), pos_,  current_club=club_name, shirt_number=number, club_coeff=coeff))
        for _ in range(12):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['Defender Midfielder', 'Center Midfielder', 'Attacking Midfielder'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad["midfielder"].append(Player(name_, natio_, randint(16,37), pos_,  current_club=club_name, shirt_number=number, club_coeff=coeff))
        for _ in range(6):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
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


if __name__ == "__main__":
    a = GenerateClass().set_players('Barcelona', 'Spain', 90)
    print(a)