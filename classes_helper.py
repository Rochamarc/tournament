from classes import *
from name_nationality import NameAndNationality as name_and_nat


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
    def set_clubs(text_file_path):
        ''' Generate a list of clubs <class 'Club'> 
            return a list(clubs)
        '''

        clubs = []

        # Creating a save file
        save_file = None # = input("Digite um valor de ate 30 caracteres pra criar um save file: ")

        if not save_file:
            save_file = None

        # files/seasons/2021.txt 
        with open(text_file_path, 'r') as file:
            for line in file.readlines():
                ''' Manage the data that are gonna be used '''
                line = line.split(',') 
                line[-1] = line[-1].replace('\n', '')
                name = line[0]
                country = line[-1]
                c = Club(name, country) # Instace the club object
                sq = GenerateClass.set_players(c.name, c.country, c.coeff) # Instance the players object 
                c.set_formation(sq) # set the formation 
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

    @staticmethod
    def set_stadium():
        stadiums = []
        with open('files/clubs_stadiums/stadiums.txt') as file:
            for line in file.readlines():
                ''' Manage the data that are gonna be used '''
                line = line.split(',')  
                line[-1] = line[-1].replace('\n', '')
                name = line[0]
                capacity = int(line[1])
                location = f'{line[2]} {line[3]}'
                club_owner = line[-1][1::] # Remove the blank space on the 0 pos
                stadiums.append(Stadium(name, location, capacity=capacity, club_owner=club_owner)) # Instance the object
        return stadiums

    @staticmethod
    def set_generic_stadium(club_country):
        s_name = f'{Name.generate_name(club_country)} stadium'
        return Stadium(s_name, club_country)

    @staticmethod
    def define_clubs_stadium(clubs, stadiums):
        for club in clubs:
            for stadium in stadiums:
                s_name = stadium.club_owner.split('/')
                if club.name in s_name:
                    club.stadium = stadium
                    break
                else:
                    club.stadium = GenerateClass().set_generic_stadium(club.country)

    @staticmethod
    def get_players_list(clubs):
        '''
        Return a list with all players data enrolled on the championship
        '''
        players = []

        for club in clubs:                                
            players += [player for player in club.start_eleven]
            players += [player for player in club.bench]
            players += [player for player in club.unrelated]
        
        return players


            

if __name__ == "__main__":
    pass 

