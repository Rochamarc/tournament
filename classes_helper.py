from classes.club import Club 
from classes.player import Player 
from classes.stadium import Stadium

from db.club_controller import ClubData
from db.domestic_league_controller import DomesticLeague
from db.stadium_controller import StadiumData
from db.player_controller import PlayerData


from name_nationality import NameAndNationality as name_and_nat
from random import randint, choice

Name = name_and_nat()
domestic = DomesticLeague()
club_data = ClubData()
std_data = StadiumData()
p_data = PlayerData()

class GenerateClass:
    @staticmethod
    def reconstruct_stadiums() -> list:
        ''' Return list of stadiums '''
        stadiums_data = std_data.get_stadiums()
        
        data = []
        
        for std in stadiums_data:
            name, location = std[0], std[1]
            capacity, owner = std[2], std[3] 
            data.append(Stadium(name, location, capacity=capacity, club_owner=owner))

        return data
    
    @staticmethod 
    def loop_for_clubs(club_data: list) -> list:
        ''' Loop through the club_data and return a list '''
        d = []
        
        for club in club_data:
            c_id, name, country, state = club[0], club[1], club[2], club[3]
            club_class, club_coeff = club[5], club[4]

            club = Club(name, country, club_class, state=state)
            club.coeff = club_coeff
            club.id = c_id
            d.append(club)
    
        return d 
            
    @classmethod
    def reconstruct_clubs(cls, division: str, season: str) -> list:
        ''' Return the list of the clubs '''
    
        clubs = domestic.get_domestic_cup_table(division, season)
        clubs_names = [ club[1] for club in clubs ]
        
        c_data = club_data.get_clubs(clubs_names) # getting clubs by name

        data = cls.loop_for_clubs(c_data)
        
        return data

    @classmethod
    def reconstruct_international_clubs(cls, country: str) -> list:
        ''' Return the list of the clubs '''
        c_data = club_data.get_clubs_by_country(country) # getting clubs by country

        data = cls.loop_for_clubs(c_data)

        return data 

    @staticmethod
    def update_player_stats(clubs: list) -> None:
        ''' Update players stats return None '''

        for club in clubs:
            for player in club.start_eleven : player.set_avg() # update average
            for player in club.bench : player.set_avg() # update average

        return None 

    @staticmethod 
    def set_clubs(text_file_path: str) -> list:
        ''' Return a list of Clubs '''
        clubs = []

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
    def set_keepers(club: Club, country: str, min_club_coeff: int, max_club_coeff: int, length=3) -> list:                
        ''' Return a list of keepers '''
        l = []
        for _ in range(length):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            
            l.append(Player(name_, natio_, randint(16,37), 'GK', min_club_coeff, max_club_coeff, current_club=club.name))
        return l
    
    @staticmethod
    def set_defenders(club: Club, country: str, min_club_coeff: int, max_club_coeff: int, length=12) -> list:
        ''' Return a list of 12 defenders, CB, LB and RB '''
        l = []

        for _ in range(length):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['CB', 'LB', 'RB'])
            
            l.append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club.name))
        return l

    
    @staticmethod
    def set_midfielders(club: Club, country: str, min_club_coeff: int, max_club_coeff: int, length=12) -> list:
        ''' Return a list of 12 midfielders, DM, CM and AM '''
        l = []

        for _ in range(length):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['DM', 'CM', 'AM'])
            
            l.append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club.name))
        return l

    @staticmethod
    def set_forwards(club: Club, country: str, min_club_coeff: int, max_club_coeff: int, length=6) -> list:
        ''' Return a list of 6 forwards, CF, SS and WG '''
        l = []

        for _ in range(length):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['CF', 'SS', 'WG'])
            
            l.append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club.name))
        return l

    @staticmethod
    def set_players(club: Club, country:str, min_club_coeff:int, max_club_coeff:int) -> list:
        ''' Return a list of players designated to the club '''
    
        squad = {
            'goal_keeper': GenerateClass().set_keepers(club, country, min_club_coeff, max_club_coeff),
            'defender': GenerateClass().set_defenders(club, country, min_club_coeff, max_club_coeff),
            'midfielder': GenerateClass().set_midfielders(club, country, min_club_coeff, max_club_coeff),
            'attacker': GenerateClass().set_forwards(club, country, min_club_coeff, max_club_coeff)
        }

        l = []

        
        for _, items in squad.items():
            for player in items:    
                player.current_club_id = club.id
                l.append(player)

        return l

    @staticmethod
    def set_stadium() -> list:
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
    def set_generic_stadium(club_country: str) -> Stadium:
        ''' Set a generic stadium '''
        s_name = f'{Name.generate_name(club_country)} stadium'
        return Stadium(s_name, club_country)

    @staticmethod
    def define_clubs_stadium(clubs: list, stadiums: list) -> None:
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
    def get_players_list(clubs: list) -> list:
        ''' Return a list with all players '''
        
        players = []

        for club in clubs:                                
            players += [player for player in club.start_eleven]
            players += [player for player in club.bench]
            # players += [player for player in club.unrelated]
        
        return players



if __name__ == "__main__":
    pass
