from classes.club import Club 
from classes.player import Player 
from classes.stadium import Stadium

from db.database import ClubData, DomesticLeague, StadiumData, PlayerData
from name_nationality import NameAndNationality as name_and_nat
from random import randint, choice

Name = name_and_nat()
domestic = DomesticLeague()
club_data = ClubData()
std_data = StadiumData()
p_data = PlayerData()

class GenerateClass:
    @staticmethod
    def reconstruct_stadiums():
        ''' Return list of stadiums '''
        stadiums_data = std_data.get_stadiums()
        
        data = []
        
        for std in stadiums_data:
            name, location = std[0], std[1]
            capacity, owner = std[2], std[3] 
            data.append(Stadium(name, location, capacity=capacity, club_owner=owner))

        return data
            
    @staticmethod
    def reconstruct_clubs(division, season):
        ''' Return the list of the clubs '''
    
        clubs = domestic.get_domestic_cup_table(division, season)
        clubs_names = [ club[1] for club in clubs ]
        
        c_data = club_data.get_clubs(clubs_names)

        data = []

        for club in c_data:
            club = club[0]
            c_id, name, country, state = club[0], club[1], club[2], club[3]
            club_class, club_coeff = club[5], club[4]

            club = Club(name, country, club_class, state=state)
            club.coeff = club_coeff
            club.id = c_id
            data.append(club)
        
        return data

    @staticmethod
    def reconstruct_international_clubs(country):
        ''' Return the list of the clubs '''
        clubs = club_data.get_clubs_by_country(country)

        data = []

        for club in clubs:
            c_id, name, country, state = club[0], club[1], club[2], club[3]
            club_class, club_coeff = club[5], club[4]

            club = Club(name, country, club_class, state=state)
            club.coeff = club_coeff
            club.id = c_id
            data.append(club)

        return data 

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
        with open(text_file_path, 'r', encoding='utf8') as file:
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
    def set_players(club, country, min_club_coeff, max_club_coeff):
        ''' Generate players <class 'Player'> to the club <class 'Club'> 
            return a dict 
        '''

        
    
        squad = {
            'goal_keeper': [],
            'defender': [],
            'midfielder': [],
            'attacker': []
        }

        for _ in range(3):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            
            
            squad['goal_keeper'].append(Player(name_, natio_, randint(16,37), 'GK', min_club_coeff, max_club_coeff, current_club=club.name))
        for _ in range(12):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['CB', 'LB', 'RB'])
            
            
            squad['defender'].append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club.name))
        for _ in range(12):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['DM', 'CM', 'AM'])
            
            
            squad["midfielder"].append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club.name))
        for _ in range(6):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['CF', 'SS', 'WG'])
            
            
            squad["attacker"].append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club.name))

        l = []

        
        for _, items in squad.items():
            for player in items:    
                player.current_club_id = club.id
                l.append(player)

        return l

    @staticmethod
    def set_generic_const_player():
        players = []

        with open('files/players/players.txt', 'r') as file:
            for line in file.readlines():

                current_club = choice(['Santos', 'Atlético Mineiro', 'Palmeiras', 'Flamengo','Fluminense', 'Santos', 'Grêmio', 'Corinthians', 'Internacional', 'São Paulo'])

                if line != '' : line = line.split(',')
                line[-1] = line[-1].replace('\n', '')

                # handling with line list
                name = line[0]
                nationality = line[1]
                age = line[2]
                position = line[3]
                overall = line[4]

                p = Player(name, nationality, age, position, 0,10)
                p.overall = overall
                p.current_club = current_club

                players.append(p)

        p_data.insert_players_db({ "players": players })
        return True

    @staticmethod
    def set_stadium():
        stadiums = []
        with open('files/clubs_stadiums/stadiums.txt', encoding='utf8') as file:
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
        ''' Set a generic stadium '''
        s_name = f'{Name.generate_name(club_country)} stadium'
        return Stadium(s_name, club_country)

    @staticmethod
    def define_clubs_stadium(clubs, stadiums):
        ''' 
        Defines a stadium to a club if the have a stadium 
        Defines a generic stadium to a club if he dosent have one
        '''
        for club in clubs:
            for stadium in stadiums:
                s_name = stadium.club_owner.split('/') # manage the string
                if club.name in s_name:
                    ''' Check if the club have a stadium '''
                    club.stadium = stadium
                    break
                else:
                    ''' Generate a generic stadium '''
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
            # players += [player for player in club.unrelated]
        
        return players



if __name__ == "__main__":
    pass
