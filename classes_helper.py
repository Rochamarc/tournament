from classes import Club, Player, Stadium
from database import ClubData, DomesticLeague, StadiumData
from name_nationality import NameAndNationality as name_and_nat
from random import randint, choice

Name = name_and_nat()
domestic = DomesticLeague()
club_data = ClubData()
std_data = StadiumData()

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
        
        cl_data = [ club_data.get_clubs(name) for name in clubs_names ]

        data = []

        for cl in cl_data:
            cl = cl[0]
            name, country, state = cl[1], cl[2], cl[3]
            club_class, club_coeff = cl[5], cl[4]

            club = Club(name, country, club_class, state=state)
            club.coeff = club_coeff
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
    def set_players(club_name, country, min_club_coeff, max_club_coeff):
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
            squad['goal_keeper'].append(Player(name_, natio_, randint(16,37), 'GK', min_club_coeff, max_club_coeff, current_club=club_name, shirt_number=number))
        for _ in range(12):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['CB', 'LB', 'RB'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad['defender'].append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club_name, shirt_number=number))
        for _ in range(12):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['DM', 'CM', 'AM'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad["midfielder"].append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club_name, shirt_number=number))
        for _ in range(6):
            natio_ = Name.generate_nationality(country)
            name_ = Name.generate_name(natio_) 
            pos_ = choice(['CF', 'SS', 'WG'])
            number = choice(shirt_numbers)
            shirt_numbers.remove(number)
            squad["attacker"].append(Player(name_, natio_, randint(16,37), pos_, min_club_coeff, max_club_coeff, current_club=club_name, shirt_number=number))


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

    @staticmethod
    def define_schedule(clubs,stadiums):
        '''
        Return a dict of lists with all the rounds filled with
        [ home_club, away_club, stadium ]
        '''

        # Not properly working yet
        # need to add max of 10 matches per round
        # and tha same club doesnt play two or more times per round
        # and the stadium cant have two or more matcher per round
        # now the method doesnt have any limitation
        # and the method will return a dict of Game() lists not list of listss

        schedule = {}

        rounds = {}
        for i in range(1,39):
            rounds[f'Round {i}'] = []

        for clb in clubs:
            ''' Define a schedule '''
            schedule[clb] = [ club for club in clubs if club.name != clb.name ]

        for home_club, away_clubs in schedule.items():
            for away_club in away_clubs:
                rnd = randint(1,38)
                rounds[f'Round {rnd}'].append([home_club, away_club, choice(stadiums)])

        return rounds 

    @staticmethod 
    def promotions_and_relegations(season, verbose=False):
        ''' Promove and relegates all the divisions of the domestic league
            return a dict with the promoted and relegated clubs
        '''
        previous_season = str(int(season) - 1) # get the previous season

        previous_serie_a = domestic.get_domestic_cup_table('serie_a', previous_season)
        previous_serie_b = domestic.get_domestic_cup_table('serie_b', previous_season)
        previous_serie_c = domestic.get_domestic_cup_table('serie_c', previous_season)

        domestic.create_domestic_table('serie_a', season) # create next season table
        domestic.create_domestic_table('serie_b', season) # create next season table
        domestic.create_domestic_table('serie_c', season) # create next season table

        current_serie_a = [ previous_serie_a[i][1] for i in range(16) ] # first 16 teams from serie_a
        current_serie_b = [ previous_serie_b[i][1] for i in range(4,16) ] # 5 to 16 from serie b
        current_serie_c = [ previous_serie_c[i][1] for i in range(4,20) ] # 5 to 20 from serie c
        
        promotions = {
            'serie_a': [],
            'serie_b': []
        }
        relegations = {
            'serie_b': [],
            'serie_c': []
        }

        for i in range(4):
            ''' promotions '''
            current_serie_a.append(previous_serie_b[i][1]) # get the first four clubs from serie b ||  b -> a
            current_serie_b.append(previous_serie_c[i][1]) # get the first four clubs from serie c ||  c -> b

            ''' relegations'''
            relegated_b = previous_serie_a.pop()
            relegated_c = previous_serie_b.pop() 

            current_serie_b.append(relegated_b[1]) # get the last four from serie b || a -> b
            current_serie_c.append(relegated_c[1]) # get the last four from serie c || b -> c

            if verbose:
                promotions['serie_a'].append(previous_serie_b[i])
                promotions['serie_b'].append(previous_serie_c[i])

                relegations['serie_b'].append(relegated_b)
                relegations['serie_c'].append(relegated_c)

        
        domestic.domestic_table_basic(current_serie_a, 'serie_a', season, verbose=verbose)
        domestic.domestic_table_basic(current_serie_b, 'serie_b', season, verbose=verbose)
        domestic.domestic_table_basic(current_serie_c, 'serie_c', season, verbose=verbose)

        return { 'promotions': promotions, 'relegations': relegations }

if __name__ == "__main__":
    pass
